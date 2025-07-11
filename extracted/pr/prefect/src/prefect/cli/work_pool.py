"""
Command line interface for working with work queues.
"""

from __future__ import annotations

import datetime
import json
import textwrap
from typing import Annotated, Any, Optional

import orjson
import typer
from rich.pretty import Pretty
from rich.table import Table

from prefect.cli._prompts import prompt_select_from_table
from prefect.cli._types import PrefectTyper
from prefect.cli._utilities import (
    exit_with_error,
    exit_with_success,
)
from prefect.cli.root import app, is_interactive
from prefect.client.collections import get_collections_metadata_client
from prefect.client.orchestration import PrefectClient, get_client
from prefect.client.schemas.actions import (
    BlockDocumentCreate,
    BlockDocumentUpdate,
    WorkPoolCreate,
    WorkPoolUpdate,
)
from prefect.client.schemas.objects import (
    BlockDocument,
    FlowRun,
    WorkPool,
    WorkPoolStorageConfiguration,
)
from prefect.exceptions import ObjectAlreadyExists, ObjectNotFound
from prefect.infrastructure.provisioners import (
    _provisioners,
    get_infrastructure_provisioner_for_work_pool_type,
)
from prefect.settings import update_current_profile
from prefect.types._datetime import now as now_fn
from prefect.utilities import urls
from prefect.workers.utilities import (
    get_available_work_pool_types,
    get_default_base_job_template_for_infrastructure_type,
)

work_pool_app: PrefectTyper = PrefectTyper(name="work-pool", help="Manage work pools.")
app.add_typer(work_pool_app, aliases=["work-pool"])


def set_work_pool_as_default(name: str) -> None:
    profile = update_current_profile({"PREFECT_DEFAULT_WORK_POOL_NAME": name})
    app.console.print(
        f"Set {name!r} as default work pool for profile {profile.name!r}\n",
        style="green",
    )
    app.console.print(
        (
            "To change your default work pool, run:\n\n\t[blue]prefect config set"
            " PREFECT_DEFAULT_WORK_POOL_NAME=<work-pool-name>[/]\n"
        ),
    )


def has_provisioner_for_type(work_pool_type: str) -> bool:
    """
    Check if there is a provisioner for the given work pool type.

    Args:
        work_pool_type (str): The type of the work pool.

    Returns:
        bool: True if a provisioner exists for the given type, False otherwise.
    """
    return work_pool_type in _provisioners


@work_pool_app.command()
async def create(
    name: str = typer.Argument(..., help="The name of the work pool."),
    base_job_template: typer.FileText = typer.Option(
        None,
        "--base-job-template",
        help=(
            "The path to a JSON file containing the base job template to use. If"
            " unspecified, Prefect will use the default base job template for the given"
            " worker type."
        ),
    ),
    paused: bool = typer.Option(
        False,
        "--paused",
        help="Whether or not to create the work pool in a paused state.",
    ),
    type: str = typer.Option(
        None, "-t", "--type", help="The type of work pool to create."
    ),
    set_as_default: bool = typer.Option(
        False,
        "--set-as-default",
        help=(
            "Whether or not to use the created work pool as the local default for"
            " deployment."
        ),
    ),
    provision_infrastructure: bool = typer.Option(
        False,
        "--provision-infrastructure",
        "--provision-infra",
        help=(
            "Whether or not to provision infrastructure for the work pool if supported"
            " for the given work pool type."
        ),
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        help=("Whether or not to overwrite an existing work pool with the same name."),
    ),
):
    """
    Create a new work pool or update an existing one.

    \b
    Examples:
        \b
        Create a Kubernetes work pool in a paused state:
            \b
            $ prefect work-pool create "my-pool" --type kubernetes --paused
        \b
        Create a Docker work pool with a custom base job template:
            \b
            $ prefect work-pool create "my-pool" --type docker --base-job-template ./base-job-template.json
        \b
        Update an existing work pool:
            \b
            $ prefect work-pool create "existing-pool" --base-job-template ./base-job-template.json --overwrite

    """
    if not name.lower().strip("'\" "):
        exit_with_error("Work pool name cannot be empty.")
    async with get_client() as client:
        try:
            existing_pool = await client.read_work_pool(work_pool_name=name)
            if not overwrite:
                exit_with_error(
                    f"Work pool named {name!r} already exists. Use --overwrite to update it."
                )
        except ObjectNotFound:
            existing_pool = None

        if type is None and existing_pool is None:
            async with get_collections_metadata_client() as collections_client:
                if not is_interactive():
                    exit_with_error(
                        "When not using an interactive terminal, you must supply a"
                        " `--type` value."
                    )
                worker_metadata = await collections_client.read_worker_metadata()

                # Retrieve only push pools if provisioning infrastructure
                data = [
                    worker
                    for collection in worker_metadata.values()
                    for worker in collection.values()
                    if provision_infrastructure
                    and has_provisioner_for_type(worker["type"])
                    or not provision_infrastructure
                ]
                worker = prompt_select_from_table(
                    app.console,
                    "What type of work pool infrastructure would you like to use?",
                    columns=[
                        {"header": "Infrastructure Type", "key": "display_name"},
                        {"header": "Description", "key": "description"},
                    ],
                    data=data,
                    table_kwargs={"show_lines": True},
                )
                type = worker["type"]
        elif existing_pool:
            type = existing_pool.type

        available_work_pool_types = await get_available_work_pool_types()
        if type not in available_work_pool_types:
            exit_with_error(
                f"Unknown work pool type {type!r}. "
                "Please choose from"
                f" {', '.join(available_work_pool_types)}."
            )

        if base_job_template is None:
            template_contents = (
                await get_default_base_job_template_for_infrastructure_type(type)
            )
        else:
            template_contents = json.load(base_job_template)

        if provision_infrastructure:
            try:
                provisioner = get_infrastructure_provisioner_for_work_pool_type(type)
                provisioner.console = app.console
                template_contents = await provisioner.provision(
                    work_pool_name=name, base_job_template=template_contents
                )
            except ValueError as exc:
                print(exc)
                app.console.print(
                    (
                        "Automatic infrastructure provisioning is not supported for"
                        f" {type!r} work pools."
                    ),
                    style="yellow",
                )
            except RuntimeError as exc:
                exit_with_error(f"Failed to provision infrastructure: {exc}")

        try:
            wp = WorkPoolCreate(
                name=name,
                type=type,
                base_job_template=template_contents,
                is_paused=paused,
            )
            work_pool = await client.create_work_pool(work_pool=wp, overwrite=overwrite)
            action = "Updated" if overwrite and existing_pool else "Created"
            app.console.print(
                f"{action} work pool {work_pool.name!r}!\n", style="green"
            )
            if (
                not work_pool.is_paused
                and not work_pool.is_managed_pool
                and not work_pool.is_push_pool
            ):
                app.console.print("To start a worker for this work pool, run:\n")
                app.console.print(
                    f"\t[blue]prefect worker start --pool {work_pool.name}[/]\n"
                )
            if set_as_default:
                set_work_pool_as_default(work_pool.name)

            url = urls.url_for(work_pool)
            pool_url = url if url else "<no dashboard available>"

            app.console.print(
                textwrap.dedent(
                    f"""
                └── UUID: {work_pool.id}
                └── Type: {work_pool.type}
                └── Description: {work_pool.description}
                └── Status: {work_pool.status.display_name}
                └── URL: {pool_url}
                """
                ).strip(),
                soft_wrap=True,
            )
            exit_with_success("")
        except ObjectAlreadyExists:
            exit_with_error(
                f"Work pool named {name!r} already exists. Please use --overwrite to update it."
            )


@work_pool_app.command()
async def ls(
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show additional information about work pools.",
    ),
):
    """
    List work pools.

    \b
    Examples:
        $ prefect work-pool ls
    """
    table = Table(
        title="Work Pools", caption="(**) denotes a paused pool", caption_style="red"
    )
    table.add_column("Name", style="green", no_wrap=True)
    table.add_column("Type", style="magenta", no_wrap=True)
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Concurrency Limit", style="blue", no_wrap=True)
    if verbose:
        table.add_column("Base Job Template", style="magenta", no_wrap=True)

    async with get_client() as client:
        pools = await client.read_work_pools()

    def sort_by_created_key(q: WorkPool) -> datetime.timedelta:
        assert q.created is not None
        return now_fn("UTC") - q.created

    for pool in sorted(pools, key=sort_by_created_key):
        row = [
            f"{pool.name} [red](**)" if pool.is_paused else pool.name,
            str(pool.type),
            str(pool.id),
            (
                f"[red]{pool.concurrency_limit}"
                if pool.concurrency_limit is not None
                else "[blue]None"
            ),
        ]
        if verbose:
            row.append(str(pool.base_job_template))
        table.add_row(*row)

    app.console.print(table)


@work_pool_app.command()
async def inspect(
    name: str = typer.Argument(..., help="The name of the work pool to inspect."),
    output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Specify an output format. Currently supports: json",
    ),
):
    """
    Inspect a work pool.

    \b
    Examples:
        $ prefect work-pool inspect "my-pool"
        $ prefect work-pool inspect "my-pool" --output json

    """
    if output and output.lower() != "json":
        exit_with_error("Only 'json' output format is supported.")

    async with get_client() as client:
        try:
            pool = await client.read_work_pool(work_pool_name=name)
            if output and output.lower() == "json":
                pool_json = pool.model_dump(mode="json")
                json_output = orjson.dumps(
                    pool_json, option=orjson.OPT_INDENT_2
                ).decode()
                app.console.print(json_output)
            else:
                app.console.print(Pretty(pool))
        except ObjectNotFound:
            exit_with_error(f"Work pool {name!r} not found!")


@work_pool_app.command()
async def pause(
    name: str = typer.Argument(..., help="The name of the work pool to pause."),
):
    """
    Pause a work pool.

    \b
    Examples:
        $ prefect work-pool pause "my-pool"

    """
    async with get_client() as client:
        try:
            await client.update_work_pool(
                work_pool_name=name,
                work_pool=WorkPoolUpdate(
                    is_paused=True,
                ),
            )
        except ObjectNotFound as exc:
            exit_with_error(exc)

        exit_with_success(f"Paused work pool {name!r}")


@work_pool_app.command()
async def resume(
    name: str = typer.Argument(..., help="The name of the work pool to resume."),
):
    """
    Resume a work pool.

    \b
    Examples:
        $ prefect work-pool resume "my-pool"

    """
    async with get_client() as client:
        try:
            await client.update_work_pool(
                work_pool_name=name,
                work_pool=WorkPoolUpdate(
                    is_paused=False,
                ),
            )
        except ObjectNotFound as exc:
            exit_with_error(exc)

        exit_with_success(f"Resumed work pool {name!r}")


@work_pool_app.command()
async def update(
    name: str = typer.Argument(..., help="The name of the work pool to update."),
    base_job_template: typer.FileText = typer.Option(
        None,
        "--base-job-template",
        help=(
            "The path to a JSON file containing the base job template to use. If"
            " unspecified, Prefect will use the default base job template for the given"
            " worker type. If None, the base job template will not be modified."
        ),
    ),
    concurrency_limit: int = typer.Option(
        None,
        "--concurrency-limit",
        help=(
            "The concurrency limit for the work pool. If None, the concurrency limit"
            " will not be modified."
        ),
    ),
    description: str = typer.Option(
        None,
        "--description",
        help=(
            "The description for the work pool. If None, the description will not be"
            " modified."
        ),
    ),
):
    """
    Update a work pool.

    \b
    Examples:
        $ prefect work-pool update "my-pool"

    """
    wp = WorkPoolUpdate()
    if base_job_template:
        wp.base_job_template = json.load(base_job_template)
    if concurrency_limit:
        wp.concurrency_limit = concurrency_limit
    if description:
        wp.description = description

    async with get_client() as client:
        try:
            await client.update_work_pool(
                work_pool_name=name,
                work_pool=wp,
            )
        except ObjectNotFound:
            exit_with_error(f"Work pool named {name!r} does not exist.")

        exit_with_success(f"Updated work pool {name!r}")


@work_pool_app.command(aliases=["provision-infra"])
async def provision_infrastructure(
    name: str = typer.Argument(
        ..., help="The name of the work pool to provision infrastructure for."
    ),
):
    """
    Provision infrastructure for a work pool.

    \b
    Examples:
        $ prefect work-pool provision-infrastructure "my-pool"

        $ prefect work-pool provision-infra "my-pool"

    """
    async with get_client() as client:
        try:
            work_pool = await client.read_work_pool(work_pool_name=name)
            if not work_pool.is_push_pool:
                exit_with_error(
                    f"Work pool {name!r} is not a push pool type. "
                    "Please try provisioning infrastructure for a push pool."
                )
        except ObjectNotFound:
            exit_with_error(f"Work pool {name!r} does not exist.")
        except Exception as exc:
            exit_with_error(f"Failed to read work pool {name!r}: {exc}")

        try:
            provisioner = get_infrastructure_provisioner_for_work_pool_type(
                work_pool.type
            )
            provisioner.console = app.console
            new_base_job_template = await provisioner.provision(
                work_pool_name=name, base_job_template=work_pool.base_job_template
            )

            await client.update_work_pool(
                work_pool_name=name,
                work_pool=WorkPoolUpdate(
                    base_job_template=new_base_job_template,
                ),
            )

        except ValueError as exc:
            app.console.print(f"Error: {exc}")
            app.console.print(
                (
                    "Automatic infrastructure provisioning is not supported for"
                    f" {work_pool.type!r} work pools."
                ),
                style="yellow",
            )
        except RuntimeError as exc:
            exit_with_error(
                f"Failed to provision infrastructure for '{name}' work pool: {exc}"
            )


@work_pool_app.command()
async def delete(
    name: str = typer.Argument(..., help="The name of the work pool to delete."),
):
    """
    Delete a work pool.

    \b
    Examples:
        $ prefect work-pool delete "my-pool"

    """
    async with get_client() as client:
        try:
            work_pool = await client.read_work_pool(work_pool_name=name)
            if is_interactive() and not typer.confirm(
                (
                    f"Are you sure you want to delete work pool with name {work_pool.name!r}?"
                ),
                default=False,
            ):
                exit_with_error("Deletion aborted.")
            await client.delete_work_pool(work_pool_name=name)
        except ObjectNotFound:
            exit_with_error(f"Work pool {name!r} does not exist.")

        exit_with_success(f"Deleted work pool {name!r}")


@work_pool_app.command()
async def set_concurrency_limit(
    name: str = typer.Argument(..., help="The name of the work pool to update."),
    concurrency_limit: int = typer.Argument(
        ..., help="The new concurrency limit for the work pool."
    ),
):
    """
    Set the concurrency limit for a work pool.

    \b
    Examples:
        $ prefect work-pool set-concurrency-limit "my-pool" 10

    """
    async with get_client() as client:
        try:
            await client.update_work_pool(
                work_pool_name=name,
                work_pool=WorkPoolUpdate(
                    concurrency_limit=concurrency_limit,
                ),
            )
        except ObjectNotFound as exc:
            exit_with_error(exc)

        exit_with_success(
            f"Set concurrency limit for work pool {name!r} to {concurrency_limit}"
        )


@work_pool_app.command()
async def clear_concurrency_limit(
    name: str = typer.Argument(..., help="The name of the work pool to update."),
):
    """
    Clear the concurrency limit for a work pool.

    \b
    Examples:
        $ prefect work-pool clear-concurrency-limit "my-pool"

    """
    async with get_client() as client:
        try:
            await client.update_work_pool(
                work_pool_name=name,
                work_pool=WorkPoolUpdate(
                    concurrency_limit=None,
                ),
            )
        except ObjectNotFound as exc:
            exit_with_error(exc)

        exit_with_success(f"Cleared concurrency limit for work pool {name!r}")


@work_pool_app.command()
async def get_default_base_job_template(
    type: str = typer.Option(
        None,
        "-t",
        "--type",
        help="The type of work pool for which to get the default base job template.",
    ),
    file: str = typer.Option(
        None, "-f", "--file", help="If set, write the output to a file."
    ),
):
    """
    Get the default base job template for a given work pool type.

    \b
    Examples:
        $ prefect work-pool get-default-base-job-template --type kubernetes
    """
    base_job_template = await get_default_base_job_template_for_infrastructure_type(
        type
    )
    if base_job_template is None:
        exit_with_error(
            f"Unknown work pool type {type!r}. "
            "Please choose from"
            f" {', '.join(await get_available_work_pool_types())}."
        )

    if file is None:
        print(json.dumps(base_job_template, indent=2))
    else:
        with open(file, mode="w") as f:
            json.dump(base_job_template, fp=f, indent=2)


@work_pool_app.command()
async def preview(
    name: str = typer.Argument(None, help="The name or ID of the work pool to preview"),
    hours: int = typer.Option(
        None,
        "-h",
        "--hours",
        help="The number of hours to look ahead; defaults to 1 hour",
    ),
):
    """
    Preview the work pool's scheduled work for all queues.

    \b
    Examples:
        $ prefect work-pool preview "my-pool" --hours 24

    """
    if hours is None:
        hours = 1

    async with get_client() as client:
        try:
            responses = await client.get_scheduled_flow_runs_for_work_pool(
                work_pool_name=name,
            )
        except ObjectNotFound as exc:
            exit_with_error(exc)

    runs = [response.flow_run for response in responses]
    table = Table(caption="(**) denotes a late run", caption_style="red")

    table.add_column(
        "Scheduled Start Time", justify="left", style="yellow", no_wrap=True
    )
    table.add_column("Run ID", justify="left", style="cyan", no_wrap=True)
    table.add_column("Name", style="green", no_wrap=True)
    table.add_column("Deployment ID", style="blue", no_wrap=True)

    now = now_fn("UTC")

    def sort_by_created_key(r: FlowRun) -> datetime.timedelta:
        assert r.created is not None
        return now - r.created

    for run in sorted(runs, key=sort_by_created_key):
        table.add_row(
            (
                f"{run.expected_start_time} [red](**)"
                if run.expected_start_time and run.expected_start_time < now
                else f"{run.expected_start_time}"
            ),
            str(run.id),
            run.name,
            str(run.deployment_id),
        )

    if runs:
        app.console.print(table)
    else:
        app.console.print(
            (
                "No runs found - try increasing how far into the future you preview"
                " with the --hours flag"
            ),
            style="yellow",
        )


# --------------------------------------------------------------------------
# Work Pool Storage Configuration
# --------------------------------------------------------------------------

work_pool_storage_app: PrefectTyper = PrefectTyper(
    name="storage", help="EXPERIMENTAL: Manage work pool storage."
)
work_pool_app.add_typer(work_pool_storage_app)


def _determine_storage_type(storage_config: WorkPoolStorageConfiguration) -> str | None:
    if storage_config.bundle_upload_step is None:
        return None
    if storage_config.bundle_upload_step and any(
        "prefect_aws" in step for step in storage_config.bundle_upload_step.keys()
    ):
        return "S3"
    if storage_config.bundle_upload_step and any(
        "prefect_gcp" in step for step in storage_config.bundle_upload_step.keys()
    ):
        return "GCS"
    if storage_config.bundle_upload_step and any(
        "prefect_azure" in step for step in storage_config.bundle_upload_step.keys()
    ):
        return "Azure Blob Storage"
    return "Unknown"


@work_pool_storage_app.command(name="inspect")
async def storage_inspect(
    work_pool_name: Annotated[
        str,
        typer.Argument(
            ..., help="The name of the work pool to display storage configuration for."
        ),
    ],
    output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Specify an output format. Currently supports: json",
    ),
):
    """
    EXPERIMENTAL: Inspect the storage configuration for a work pool.

    Examples:
        $ prefect work-pool storage inspect "my-pool"
        $ prefect work-pool storage inspect "my-pool" --output json
    """
    if output and output.lower() != "json":
        exit_with_error("Only 'json' output format is supported.")

    async with get_client() as client:
        try:
            work_pool = await client.read_work_pool(work_pool_name=work_pool_name)
            from rich.panel import Panel
            from rich.table import Table

            storage_table = Table(show_header=True, header_style="bold")
            storage_table.add_column("Setting", style="cyan")
            storage_table.add_column("Value")

            storage_type = _determine_storage_type(work_pool.storage_configuration)
            if not storage_type:
                if output and output.lower() == "json":
                    app.console.print("{}")
                else:
                    app.console.print(
                        f"No storage configuration found for work pool {work_pool_name!r}",
                        style="yellow",
                    )
                return

            if output and output.lower() == "json":
                storage_data = {"type": storage_type}
                if work_pool.storage_configuration.bundle_upload_step is not None:
                    fqn = list(
                        work_pool.storage_configuration.bundle_upload_step.keys()
                    )[0]
                    config_values = work_pool.storage_configuration.bundle_upload_step[
                        fqn
                    ]
                    storage_data.update(config_values)

                json_output = orjson.dumps(
                    storage_data, option=orjson.OPT_INDENT_2
                ).decode()
                app.console.print(json_output)
            else:
                storage_table.add_row("type", storage_type)

                # Add other storage settings, filtering out None values
                if work_pool.storage_configuration.bundle_upload_step is not None:
                    fqn = list(
                        work_pool.storage_configuration.bundle_upload_step.keys()
                    )[0]
                    config_values = work_pool.storage_configuration.bundle_upload_step[
                        fqn
                    ]
                    for key, value in config_values.items():
                        storage_table.add_row(key, str(value))

                panel = Panel(
                    storage_table,
                    title=f"[bold]Storage Configuration for {work_pool_name}[/bold]",
                    expand=False,
                )

                app.console.print(panel)

        except ObjectNotFound:
            exit_with_error(f"Work pool {work_pool_name!r} does not exist.")


async def _create_or_update_result_storage_block(
    client: PrefectClient,
    block_document_name: str,
    block_document_data: dict[str, Any],
    block_type_slug: str,
    missing_block_definition_error: str,
) -> BlockDocument:
    try:
        existing_block_document = await client.read_block_document_by_name(
            name=block_document_name, block_type_slug=block_type_slug
        )
    except ObjectNotFound:
        existing_block_document = None

    if existing_block_document is not None:
        await client.update_block_document(
            block_document_id=existing_block_document.id,
            block_document=BlockDocumentUpdate(
                data=block_document_data,
            ),
        )
        block_document = existing_block_document
    else:
        try:
            block_type = await client.read_block_type_by_slug(slug=block_type_slug)
            block_schema = await client.get_most_recent_block_schema_for_block_type(
                block_type_id=block_type.id
            )
        except ObjectNotFound:
            exit_with_error(missing_block_definition_error)
        else:
            if block_schema is None:
                exit_with_error(missing_block_definition_error)

        block_document = await client.create_block_document(
            block_document=BlockDocumentCreate(
                name=block_document_name,
                block_type_id=block_type.id,
                block_schema_id=block_schema.id,
                data=block_document_data,
            )
        )

    return block_document


work_pool_storage_configure_app: PrefectTyper = PrefectTyper(
    name="configure", help="EXPERIMENTAL: Configure work pool storage."
)
work_pool_storage_app.add_typer(work_pool_storage_configure_app)


@work_pool_storage_configure_app.command()
async def s3(
    work_pool_name: str = typer.Argument(
        ...,
        help="The name of the work pool to configure storage for.",
        show_default=False,
    ),
    bucket: str = typer.Option(
        ...,
        "--bucket",
        help="The name of the S3 bucket to use.",
        show_default=False,
        prompt="Enter the name of the S3 bucket to use",
    ),
    credentials_block_name: str = typer.Option(
        ...,
        "--aws-credentials-block-name",
        help="The name of the AWS credentials block to use.",
        show_default=False,
        prompt="Enter the name of the AWS credentials block to use",
    ),
):
    """
    EXPERIMENTAL: Configure AWS S3 storage for a work pool.

    \b
    Examples:
        $ prefect work-pool storage configure s3 "my-pool" --bucket my-bucket --aws-credentials-block-name my-credentials
    """
    # TODO: Allow passing in AWS keys and creating a block for the user.
    async with get_client() as client:
        try:
            credentials_block_document = await client.read_block_document_by_name(
                name=credentials_block_name, block_type_slug="aws-credentials"
            )
        except ObjectNotFound:
            exit_with_error(
                f"AWS credentials block {credentials_block_name!r} does not exist. Please create one using `prefect block create aws-credentials`."
            )

        result_storage_block_document_name = f"default-{work_pool_name}-result-storage"
        block_data = {
            "bucket_name": bucket,
            "bucket_folder": "results",
            "credentials": {
                "$ref": {"block_document_id": credentials_block_document.id}
            },
        }

        block_document = await _create_or_update_result_storage_block(
            client=client,
            block_document_name=result_storage_block_document_name,
            block_document_data=block_data,
            block_type_slug="s3-bucket",
            missing_block_definition_error="S3 bucket block definition does not exist server-side. Please install `prefect-aws` and run `prefect blocks register -m prefect_aws`.",
        )

        try:
            await client.update_work_pool(
                work_pool_name=work_pool_name,
                work_pool=WorkPoolUpdate(
                    storage_configuration=WorkPoolStorageConfiguration(
                        bundle_upload_step={
                            "prefect_aws.experimental.bundles.upload": {
                                "requires": "prefect-aws",
                                "bucket": bucket,
                                "aws_credentials_block_name": credentials_block_name,
                            }
                        },
                        bundle_execution_step={
                            "prefect_aws.experimental.bundles.execute": {
                                "requires": "prefect-aws",
                                "bucket": bucket,
                                "aws_credentials_block_name": credentials_block_name,
                            }
                        },
                        default_result_storage_block_id=block_document.id,
                    ),
                ),
            )
        except ObjectNotFound:
            exit_with_error(f"Work pool {work_pool_name!r} does not exist.")

        exit_with_success(f"Configured S3 storage for work pool {work_pool_name!r}")


@work_pool_storage_configure_app.command()
async def gcs(
    work_pool_name: str = typer.Argument(
        ...,
        help="The name of the work pool to configure storage for.",
        show_default=False,
    ),
    bucket: str = typer.Option(
        ...,
        "--bucket",
        help="The name of the Google Cloud Storage bucket to use.",
        show_default=False,
        prompt="Enter the name of the Google Cloud Storage bucket to use",
    ),
    credentials_block_name: str = typer.Option(
        ...,
        "--gcp-credentials-block-name",
        help="The name of the Google Cloud credentials block to use.",
        show_default=False,
        prompt="Enter the name of the Google Cloud credentials block to use",
    ),
):
    """
    EXPERIMENTAL: Configure Google Cloud storage for a work pool.

    \b
    Examples:
        $ prefect work-pool storage configure gcs "my-pool" --bucket my-bucket --gcp-credentials-block-name my-credentials
    """
    async with get_client() as client:
        try:
            credentials_block_document = await client.read_block_document_by_name(
                name=credentials_block_name, block_type_slug="gcp-credentials"
            )
        except ObjectNotFound:
            exit_with_error(
                f"GCS credentials block {credentials_block_name!r} does not exist. Please create one using `prefect block create gcp-credentials`."
            )

        result_storage_block_document_name = f"default-{work_pool_name}-result-storage"
        block_data = {
            "bucket_name": bucket,
            "bucket_folder": "results",
            "credentials": {
                "$ref": {"block_document_id": credentials_block_document.id}
            },
        }

        block_document = await _create_or_update_result_storage_block(
            client=client,
            block_document_name=result_storage_block_document_name,
            block_document_data=block_data,
            block_type_slug="gcs-bucket",
            missing_block_definition_error="GCS bucket block definition does not exist server-side. Please install `prefect-gcp` and run `prefect blocks register -m prefect_gcp`.",
        )

        try:
            await client.update_work_pool(
                work_pool_name=work_pool_name,
                work_pool=WorkPoolUpdate(
                    storage_configuration=WorkPoolStorageConfiguration(
                        bundle_upload_step={
                            "prefect_gcp.experimental.bundles.upload": {
                                "requires": "prefect-gcp",
                                "bucket": bucket,
                                "gcp_credentials_block_name": credentials_block_name,
                            }
                        },
                        bundle_execution_step={
                            "prefect_gcp.experimental.bundles.execute": {
                                "requires": "prefect-gcp",
                                "bucket": bucket,
                                "gcp_credentials_block_name": credentials_block_name,
                            }
                        },
                        default_result_storage_block_id=block_document.id,
                    ),
                ),
            )
        except ObjectNotFound:
            exit_with_error(f"Work pool {work_pool_name!r} does not exist.")

        exit_with_success(f"Configured GCS storage for work pool {work_pool_name!r}")


@work_pool_storage_configure_app.command()
async def azure_blob_storage(
    work_pool_name: str = typer.Argument(
        ...,
        help="The name of the work pool to configure storage for.",
        show_default=False,
    ),
    container: str = typer.Option(
        ...,
        "--container",
        help="The name of the Azure Blob Storage container to use.",
        show_default=False,
        prompt="Enter the name of the Azure Blob Storage container to use",
    ),
    credentials_block_name: str = typer.Option(
        ...,
        "--azure-blob-storage-credentials-block-name",
        help="The name of the Azure Blob Storage credentials block to use.",
        show_default=False,
        prompt="Enter the name of the Azure Blob Storage credentials block to use",
    ),
):
    """
    EXPERIMENTAL: Configure Azure Blob Storage for a work pool.

    \b
    Examples:
        $ prefect work-pool storage configure azure-blob-storage "my-pool" --container my-container --azure-blob-storage-credentials-block-name my-credentials
    """
    async with get_client() as client:
        try:
            credentials_block_document = await client.read_block_document_by_name(
                name=credentials_block_name,
                block_type_slug="azure-blob-storage-credentials",
            )
        except ObjectNotFound:
            exit_with_error(
                f"Azure Blob Storage credentials block {credentials_block_name!r} does not exist. Please create one using `prefect block create azure-blob-storage-credentials`."
            )

        result_storage_block_document_name = f"default-{work_pool_name}-result-storage"
        block_data = {
            "container_name": container,
            "credentials": {
                "$ref": {"block_document_id": credentials_block_document.id}
            },
        }

        block_document = await _create_or_update_result_storage_block(
            client=client,
            block_document_name=result_storage_block_document_name,
            block_document_data=block_data,
            block_type_slug="azure-blob-storage-container",
            missing_block_definition_error="Azure Blob Storage container block definition does not exist server-side. Please install `prefect-azure[storage]` and run `prefect blocks register -m prefect_azure`.",
        )

        try:
            await client.update_work_pool(
                work_pool_name=work_pool_name,
                work_pool=WorkPoolUpdate(
                    storage_configuration=WorkPoolStorageConfiguration(
                        bundle_upload_step={
                            "prefect_azure.experimental.bundles.upload": {
                                "requires": "prefect-azure",
                                "container": container,
                                "azure_blob_storage_credentials_block_name": credentials_block_name,
                            }
                        },
                        bundle_execution_step={
                            "prefect_azure.experimental.bundles.execute": {
                                "requires": "prefect-azure",
                                "container": container,
                                "azure_blob_storage_credentials_block_name": credentials_block_name,
                            }
                        },
                        default_result_storage_block_id=block_document.id,
                    ),
                ),
            )
        except ObjectNotFound:
            exit_with_error(f"Work pool {work_pool_name!r} does not exist.")

        exit_with_success(
            f"Configured Azure Blob Storage for work pool {work_pool_name!r}"
        )
