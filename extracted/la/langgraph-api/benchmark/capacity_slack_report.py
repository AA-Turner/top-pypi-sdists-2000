#!/usr/bin/env python3
"""
Generate and send capacity benchmark summary to Slack.
"""

import json
import os
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import cast
from urllib.error import URLError
from urllib.request import Request, urlopen


def load_capacity_results(results_dir: str) -> list[dict]:
    """Load all capacity summary JSON files and extract metadata from filenames."""
    results = []

    results_path = Path(results_dir)
    if not results_path.exists():
        return results

    for f in results_path.glob("**/*_capacity_summary.json"):
        try:
            with open(f) as fp:
                data = json.load(fp)

            # Extract cluster_name and workload_name from filename
            # Format: {cluster_name}_{workload_name}_capacity_summary.json
            # Example: dr-small_sequential-small_capacity_summary.json
            name_part = f.stem.replace("_capacity_summary", "")
            parts = name_part.split("_", 1)  # Split only on first underscore
            if len(parts) >= 2:
                cluster_name = parts[0]
                workload_name = parts[1]

                results.append(
                    {
                        "clusterName": cluster_name,
                        "workloadName": workload_name,
                        "maxSuccessfulTarget": data.get("maxSuccessfulTarget"),
                        "avgExecutionLatencySeconds": data.get(
                            "avgExecutionLatencySeconds"
                        ),
                    }
                )
        except (OSError, json.JSONDecodeError):
            continue

    return results


def format_latency(value: float | None) -> str:
    """Format latency in seconds."""
    if value is None:
        return "N/A"
    return f"{value:.3f}s"


def format_target(value: int | None) -> str:
    """Format target value."""
    if value is None:
        return "N/A"
    return str(value)


def generate_capacity_table(results: list[dict]) -> str:
    """Generate a formatted table for capacity benchmark results."""
    if not results:
        return "*No capacity results collected*"

    # Group by workload, then by cluster
    by_workload = defaultdict(dict)
    for r in results:
        workload = r["workloadName"]
        cluster = r["clusterName"]
        by_workload[workload][cluster] = r

    lines = ["*📊 Capacity Benchmark Results*\n"]

    # Define cluster order for consistent display
    cluster_order = [
        "dr-small",
        "dr-medium",
        "dr-large",
        "py-small",
        "py-medium",
        "py-large",
    ]

    for workload in sorted(by_workload.keys()):
        clusters_data = by_workload[workload]
        lines.append(f"\n*Workload: `{workload}`*")
        lines.append("```")
        lines.append(f"{'Cluster':<12} | {'Max Target':>10} | {'Avg Latency':>12}")
        lines.append("-" * 40)

        for cluster in cluster_order:
            if cluster in clusters_data:
                data = clusters_data[cluster]
                lines.append(
                    f"{cluster:<12} | "
                    f"{format_target(data['maxSuccessfulTarget']):>10} | "
                    f"{format_latency(data['avgExecutionLatencySeconds']):>12}"
                )
        lines.append("```")

    return "\n".join(lines)


def send_to_slack(message: str, channel: str, token: str) -> bool:
    """Send message to Slack using the Web API."""
    try:
        payload = json.dumps(
            {
                "channel": channel,
                "text": message,
            }
        ).encode("utf-8")

        request = Request(
            "https://slack.com/api/chat.postMessage",
            data=payload,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {token}",
            },
        )

        with urlopen(request, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))

        if not result.get("ok"):
            error = result.get("error", "Unknown error")
            print(f"❌ Slack API error: {error}", file=sys.stderr)  # noqa: T201
            return False

        print("✅ Message sent to Slack successfully")  # noqa: T201
        return True
    except (URLError, Exception) as e:
        print(f"❌ Failed to send to Slack: {e}", file=sys.stderr)  # noqa: T201
        return False


def generate_slack_message(results: list[dict], run_url: str) -> str:
    """Generate the complete Slack message."""
    status_emoji = "🟢" if results else "🔴"
    status = "Completed" if results else "No results collected"

    lines = [
        f"📊 *Capacity Benchmark Summary* {status_emoji}",
        f"*Status*: {status}",
        "",
        generate_capacity_table(results),
        "",
        f"📁 *GitHub Actions Run*: <{run_url}|View Details>",
        "",
        f"🕐 *Run Time*: {datetime.now(UTC).strftime('%Y-%m-%d %H:%M UTC')}",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(  # noqa: T201
            "Usage: capacity_slack_report.py <results_dir> <github_run_url>",
            file=sys.stderr,
        )
        sys.exit(1)

    results_dir = sys.argv[1]
    run_url = sys.argv[2]

    # Get Slack credentials
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    slack_channel = os.getenv("SLACK_CHANNEL")

    if not slack_token or not slack_channel:
        print("Error: SLACK_BOT_TOKEN and SLACK_CHANNEL must be set", file=sys.stderr)  # noqa: T201
        sys.exit(1)

    # Load results
    results = load_capacity_results(results_dir)

    # Generate message
    message = generate_slack_message(results, run_url)

    # Send to Slack (cast needed because type checker doesn't know we've validated these are not None)
    if not send_to_slack(message, cast("str", slack_channel), cast("str", slack_token)):
        sys.exit(1)
