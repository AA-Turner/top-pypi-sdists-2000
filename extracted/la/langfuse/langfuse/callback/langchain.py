import logging
import typing
import warnings
from collections import defaultdict

import httpx
import pydantic

try:  # Test that langchain is installed before proceeding
    import langchain  # noqa
except ImportError as e:
    log = logging.getLogger("langfuse")
    log.error(
        f"Could not import langchain. The langchain integration will not work. {e}"
    )
from typing import Any, Dict, List, Optional, Sequence, Set, Type, Union, cast
from uuid import UUID, uuid4

from langfuse.api.resources.ingestion.types.sdk_log_body import SdkLogBody
from langfuse.client import (
    StatefulGenerationClient,
    StatefulSpanClient,
    StatefulTraceClient,
)
from langfuse.extract_model import _extract_model_name
from langfuse.types import MaskFunction
from langfuse.utils import _get_timestamp
from langfuse.utils.base_callback_handler import LangfuseBaseCallbackHandler

try:
    from langchain.callbacks.base import (
        BaseCallbackHandler as LangchainBaseCallbackHandler,
    )
    from langchain.schema.agent import AgentAction, AgentFinish
    from langchain.schema.document import Document
    from langchain_core.messages import (
        AIMessage,
        BaseMessage,
        ChatMessage,
        FunctionMessage,
        HumanMessage,
        SystemMessage,
        ToolMessage,
    )
    from langchain_core.outputs import (
        ChatGeneration,
        LLMResult,
    )
except ImportError:
    raise ModuleNotFoundError(
        "Please install langchain to use the Langfuse langchain integration: 'pip install langchain'"
    )

LANGSMITH_TAG_HIDDEN: str = "langsmith:hidden"
CONTROL_FLOW_EXCEPTION_TYPES: Set[Type[BaseException]] = set()

try:
    from langgraph.errors import GraphBubbleUp

    CONTROL_FLOW_EXCEPTION_TYPES.add(GraphBubbleUp)
except ImportError:
    pass


class LangchainCallbackHandler(
    LangchainBaseCallbackHandler, LangfuseBaseCallbackHandler
):
    log = logging.getLogger("langfuse")
    next_span_id: Optional[str] = None

    def __init__(
        self,
        public_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        host: Optional[str] = None,
        debug: bool = False,
        stateful_client: Optional[
            Union[StatefulTraceClient, StatefulSpanClient]
        ] = None,
        update_stateful_client: bool = False,
        session_id: Optional[str] = None,
        user_id: Optional[str] = None,
        trace_name: Optional[str] = None,
        release: Optional[str] = None,
        version: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None,
        threads: Optional[int] = None,
        flush_at: Optional[int] = None,
        flush_interval: Optional[int] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[int] = None,
        enabled: Optional[bool] = None,
        httpx_client: Optional[httpx.Client] = None,
        sdk_integration: Optional[str] = None,
        sample_rate: Optional[float] = None,
        mask: Optional[MaskFunction] = None,
        environment: Optional[str] = None,
    ) -> None:
        LangfuseBaseCallbackHandler.__init__(
            self,
            public_key=public_key,
            secret_key=secret_key,
            host=host,
            debug=debug,
            stateful_client=stateful_client,
            update_stateful_client=update_stateful_client,
            session_id=session_id,
            user_id=user_id,
            trace_name=trace_name,
            release=release,
            version=version,
            metadata=metadata,
            tags=tags,
            threads=threads,
            flush_at=flush_at,
            flush_interval=flush_interval,
            max_retries=max_retries,
            timeout=timeout,
            enabled=enabled,
            httpx_client=httpx_client,
            sdk_integration=sdk_integration or "langchain",
            sample_rate=sample_rate,
            mask=mask,
            environment=environment,
        )

        self.runs = {}
        self.prompt_to_parent_run_map = {}
        self.trace_updates = defaultdict(dict)
        self.updated_completion_start_time_memo = set()

        if stateful_client and isinstance(stateful_client, StatefulSpanClient):
            self.runs[stateful_client.id] = stateful_client

    def setNextSpan(self, id: str):
        warnings.warn(
            "setNextSpan is deprecated, use span.get_langchain_handler() instead",
            DeprecationWarning,
        )
        self.next_span_id = id

    def on_llm_new_token(
        self,
        token: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on new LLM token. Only available when streaming is enabled."""
        self.log.debug(
            f"on llm new token: run_id: {run_id} parent_run_id: {parent_run_id}"
        )
        if (
            run_id in self.runs
            and isinstance(self.runs[run_id], StatefulGenerationClient)
            and run_id not in self.updated_completion_start_time_memo
        ):
            current_generation = cast(StatefulGenerationClient, self.runs[run_id])
            current_generation.update(completion_start_time=_get_timestamp())

            self.updated_completion_start_time_memo.add(run_id)

    def get_langchain_run_name(
        self, serialized: Optional[Dict[str, Any]], **kwargs: Any
    ) -> str:
        """Retrieve the name of a serialized LangChain runnable.

        The prioritization for the determination of the run name is as follows:
        - The value assigned to the "name" key in `kwargs`.
        - The value assigned to the "name" key in `serialized`.
        - The last entry of the value assigned to the "id" key in `serialized`.
        - "<unknown>".

        Args:
            serialized (Optional[Dict[str, Any]]): A dictionary containing the runnable's serialized data.
            **kwargs (Any): Additional keyword arguments, potentially including the 'name' override.

        Returns:
            str: The determined name of the Langchain runnable.
        """
        if "name" in kwargs and kwargs["name"] is not None:
            return kwargs["name"]

        try:
            return serialized["name"]
        except (KeyError, TypeError):
            pass

        try:
            return serialized["id"][-1]
        except (KeyError, TypeError):
            pass

        return "<unknown>"

    def on_retriever_error(
        self,
        error: Union[Exception, KeyboardInterrupt],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run when Retriever errors."""
        try:
            self._log_debug_event(
                "on_retriever_error", run_id, parent_run_id, error=error
            )

            if run_id is None or run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                level="ERROR",
                status_message=str(error),
                version=self.version,
                input=kwargs.get("inputs"),
            )
        except Exception as e:
            self.log.exception(e)

    def on_chain_start(
        self,
        serialized: Optional[Dict[str, Any]],
        inputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_chain_start", run_id, parent_run_id, inputs=inputs
            )
            self.__generate_trace_and_parent(
                serialized=serialized,
                inputs=inputs,
                run_id=run_id,
                parent_run_id=parent_run_id,
                tags=tags,
                metadata=metadata,
                version=self.version,
                **kwargs,
            )
            self._register_langfuse_prompt(
                run_id=run_id, parent_run_id=parent_run_id, metadata=metadata
            )

            # Update trace-level information if this is a root-level chain (no parent)
            # and if tags or metadata are provided
            if parent_run_id is None and (tags or metadata):
                self.trace_updates[run_id].update(
                    {
                        "tags": [str(tag) for tag in tags] if tags else None,
                        "session_id": metadata.get("langfuse_session_id")
                        if metadata
                        else None,
                        "user_id": metadata.get("langfuse_user_id")
                        if metadata
                        else None,
                    }
                )

            content = {
                "id": self.next_span_id,
                "trace_id": self.trace.id,
                "name": self.get_langchain_run_name(serialized, **kwargs),
                "metadata": self.__join_tags_and_metadata(tags, metadata),
                "input": inputs,
                "version": self.version,
                "level": "DEBUG" if tags and LANGSMITH_TAG_HIDDEN in tags else None,
            }
            if parent_run_id is None:
                if self.root_span is None:
                    self.runs[run_id] = self.trace.span(**content)
                else:
                    self.runs[run_id] = self.root_span.span(**content)
            if parent_run_id is not None:
                self.runs[run_id] = self.runs[parent_run_id].span(**content)

        except Exception as e:
            self.log.exception(e)

    def _register_langfuse_prompt(
        self,
        *,
        run_id,
        parent_run_id: Optional[UUID],
        metadata: Optional[Dict[str, Any]],
    ):
        """We need to register any passed Langfuse prompt to the parent_run_id so that we can link following generations with that prompt.

        If parent_run_id is None, we are at the root of a trace and should not attempt to register the prompt, as there will be no LLM invocation following it.
        Otherwise it would have been traced in with a parent run consisting of the prompt template formatting and the LLM invocation.
        """
        if not parent_run_id:
            return

        langfuse_prompt = metadata and metadata.get("langfuse_prompt", None)

        if langfuse_prompt:
            self.prompt_to_parent_run_map[parent_run_id] = langfuse_prompt

        # If we have a registered prompt that has not been linked to a generation yet, we need to allow _children_ of that chain to link to it.
        # Otherwise, we only allow generations on the same level of the prompt rendering to be linked, not if they are nested.
        elif parent_run_id in self.prompt_to_parent_run_map:
            registered_prompt = self.prompt_to_parent_run_map[parent_run_id]
            self.prompt_to_parent_run_map[run_id] = registered_prompt

    def _deregister_langfuse_prompt(self, run_id: Optional[UUID]):
        if run_id in self.prompt_to_parent_run_map:
            del self.prompt_to_parent_run_map[run_id]

    def __generate_trace_and_parent(
        self,
        serialized: Optional[Dict[str, Any]],
        inputs: Union[Dict[str, Any], List[str], str, None],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        try:
            class_name = self.get_langchain_run_name(serialized, **kwargs)

            # on a new invocation, and not user provided root, we want to initialise a new traceo
            # parent_run_id is None when we are at the root of a langchain execution
            if (
                self.trace is not None
                and parent_run_id is None
                and self.langfuse is not None
            ):
                self.trace = None

            if (
                self.trace is not None
                and parent_run_id is None  # We are at the root of a langchain execution
                and self.langfuse is None  # StatefulClient was provided by user
                and self.update_stateful_client
            ):
                params = {
                    "name": self.trace_name
                    if self.trace_name is not None
                    else class_name,
                    "metadata": self.__join_tags_and_metadata(
                        tags, metadata, trace_metadata=self.metadata
                    ),
                    "version": self.version,
                    "session_id": self.session_id,
                    "user_id": self.user_id,
                    "tags": self.tags,
                    "input": inputs,
                }

                if self.root_span:
                    self.root_span.update(**params)
                else:
                    self.trace.update(**params)

            # if we are at a root, but langfuse exists, it means we do not have a
            # root provided by a user. Initialise it by creating a trace and root span.
            if self.trace is None and self.langfuse is not None:
                trace = self.langfuse.trace(
                    id=str(run_id),
                    name=self.trace_name if self.trace_name is not None else class_name,
                    metadata=self.__join_tags_and_metadata(
                        tags, metadata, trace_metadata=self.metadata
                    ),
                    version=self.version,
                    session_id=self.session_id,
                    user_id=self.user_id,
                    tags=self.tags,
                    input=inputs,
                )

                self.trace = trace

                if parent_run_id is not None and parent_run_id in self.runs:
                    self.runs[run_id] = self.trace.span(
                        id=self.next_span_id,
                        trace_id=self.trace.id,
                        name=class_name,
                        metadata=self.__join_tags_and_metadata(tags, metadata),
                        input=inputs,
                        version=self.version,
                    )

                return

        except Exception as e:
            self.log.exception(e)

    def on_agent_action(
        self,
        action: AgentAction,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run on agent action."""
        try:
            self._log_debug_event(
                "on_agent_action", run_id, parent_run_id, action=action
            )

            if run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                output=action,
                version=self.version,
                input=kwargs.get("inputs"),
            )

        except Exception as e:
            self.log.exception(e)

    def on_agent_finish(
        self,
        finish: AgentFinish,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_agent_finish", run_id, parent_run_id, finish=finish
            )
            if run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                output=finish,
                version=self.version,
                input=kwargs.get("inputs"),
            )

            # langchain sends same run_id for agent_finish and chain_end for the same agent interaction.
            # Hence, we only delete at chain_end and not here.
            self._update_trace_and_remove_state(
                run_id, parent_run_id, finish, keep_state=True
            )

        except Exception as e:
            self.log.exception(e)

    def on_chain_end(
        self,
        outputs: Dict[str, Any],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_chain_end", run_id, parent_run_id, outputs=outputs
            )

            if run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                output=outputs,
                version=self.version,
                input=kwargs.get("inputs"),
            )
            self._update_trace_and_remove_state(
                run_id, parent_run_id, outputs, input=kwargs.get("inputs")
            )
            self._deregister_langfuse_prompt(run_id)
        except Exception as e:
            self.log.exception(e)

    def on_chain_error(
        self,
        error: Union[Exception, KeyboardInterrupt],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        try:
            self._log_debug_event("on_chain_error", run_id, parent_run_id, error=error)
            if run_id in self.runs:
                if any(isinstance(error, t) for t in CONTROL_FLOW_EXCEPTION_TYPES):
                    level = None
                else:
                    level = "ERROR"

                self.runs[run_id] = self.runs[run_id].end(
                    level=level,
                    status_message=str(error),
                    version=self.version,
                    input=kwargs.get("inputs"),
                )

                self._update_trace_and_remove_state(
                    run_id, parent_run_id, error, input=kwargs.get("inputs")
                )
            else:
                self.log.warning(
                    f"Run ID {run_id} already popped from run map. Could not update run with error message"
                )

        except Exception as e:
            self.log.exception(e)

    def on_chat_model_start(
        self,
        serialized: Optional[Dict[str, Any]],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_chat_model_start", run_id, parent_run_id, messages=messages
            )
            self.__on_llm_action(
                serialized,
                run_id,
                _flatten_comprehension(
                    [self._create_message_dicts(m) for m in messages]
                ),
                parent_run_id,
                tags=tags,
                metadata=metadata,
                **kwargs,
            )
        except Exception as e:
            self.log.exception(e)

    def on_llm_start(
        self,
        serialized: Optional[Dict[str, Any]],
        prompts: List[str],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_llm_start", run_id, parent_run_id, prompts=prompts
            )
            self.__on_llm_action(
                serialized,
                run_id,
                prompts[0] if len(prompts) == 1 else prompts,
                parent_run_id,
                tags=tags,
                metadata=metadata,
                **kwargs,
            )
        except Exception as e:
            self.log.exception(e)

    def on_tool_start(
        self,
        serialized: Optional[Dict[str, Any]],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_tool_start", run_id, parent_run_id, input_str=input_str
            )

            if parent_run_id is None or parent_run_id not in self.runs:
                raise Exception("parent run not found")
            meta = self.__join_tags_and_metadata(tags, metadata)

            if not meta:
                meta = {}

            meta.update(
                {key: value for key, value in kwargs.items() if value is not None}
            )

            self.runs[run_id] = self.runs[parent_run_id].span(
                id=self.next_span_id,
                name=self.get_langchain_run_name(serialized, **kwargs),
                input=input_str,
                metadata=meta,
                version=self.version,
                level="DEBUG" if tags and LANGSMITH_TAG_HIDDEN in tags else None,
            )
            self.next_span_id = None
        except Exception as e:
            self.log.exception(e)

    def on_retriever_start(
        self,
        serialized: Optional[Dict[str, Any]],
        query: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_retriever_start", run_id, parent_run_id, query=query
            )
            if parent_run_id is None:
                self.__generate_trace_and_parent(
                    serialized=serialized,
                    inputs=query,
                    run_id=run_id,
                    parent_run_id=parent_run_id,
                    tags=tags,
                    metadata=metadata,
                    version=self.version,
                    **kwargs,
                )
                content = {
                    "id": self.next_span_id,
                    "trace_id": self.trace.id,
                    "name": self.get_langchain_run_name(serialized, **kwargs),
                    "metadata": self.__join_tags_and_metadata(tags, metadata),
                    "input": query,
                    "version": self.version,
                    "level": "DEBUG" if tags and LANGSMITH_TAG_HIDDEN in tags else None,
                }
                if self.root_span is None:
                    self.runs[run_id] = self.trace.span(**content)
                else:
                    self.runs[run_id] = self.root_span.span(**content)
            else:
                self.runs[run_id] = self.runs[parent_run_id].span(
                    id=self.next_span_id,
                    name=self.get_langchain_run_name(serialized, **kwargs),
                    input=query,
                    metadata=self.__join_tags_and_metadata(tags, metadata),
                    version=self.version,
                    level="DEBUG" if tags and LANGSMITH_TAG_HIDDEN in tags else None,
                )
                self.next_span_id = None
        except Exception as e:
            self.log.exception(e)

    def on_retriever_end(
        self,
        documents: Sequence[Document],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_retriever_end", run_id, parent_run_id, documents=documents
            )
            if run_id is None or run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                output=documents,
                version=self.version,
                input=kwargs.get("inputs"),
            )

            self._update_trace_and_remove_state(run_id, parent_run_id, documents)

        except Exception as e:
            self.log.exception(e)

    def on_tool_end(
        self,
        output: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event("on_tool_end", run_id, parent_run_id, output=output)
            if run_id is None or run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                output=output,
                version=self.version,
                input=kwargs.get("inputs"),
            )

            self._update_trace_and_remove_state(run_id, parent_run_id, output)

        except Exception as e:
            self.log.exception(e)

    def on_tool_error(
        self,
        error: Union[Exception, KeyboardInterrupt],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event("on_tool_error", run_id, parent_run_id, error=error)
            if run_id is None or run_id not in self.runs:
                raise Exception("run not found")

            self.runs[run_id] = self.runs[run_id].end(
                status_message=str(error),
                level="ERROR",
                version=self.version,
                input=kwargs.get("inputs"),
            )

            self._update_trace_and_remove_state(run_id, parent_run_id, error)

        except Exception as e:
            self.log.exception(e)

    def __on_llm_action(
        self,
        serialized: Optional[Dict[str, Any]],
        run_id: UUID,
        prompts: List[str],
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        try:
            tools = kwargs.get("invocation_params", {}).get("tools", None)
            if tools and isinstance(tools, list):
                prompts.extend([{"role": "tool", "content": tool} for tool in tools])

            self.__generate_trace_and_parent(
                serialized,
                inputs=prompts[0] if len(prompts) == 1 else prompts,
                run_id=run_id,
                parent_run_id=parent_run_id,
                tags=tags,
                metadata=metadata,
                version=self.version,
                kwargs=kwargs,
            )

            model_name = None

            model_name = self._parse_model_and_log_errors(
                serialized=serialized, metadata=metadata, kwargs=kwargs
            )
            registered_prompt = self.prompt_to_parent_run_map.get(parent_run_id, None)

            if registered_prompt:
                self._deregister_langfuse_prompt(parent_run_id)

            content = {
                "name": self.get_langchain_run_name(serialized, **kwargs),
                "input": prompts,
                "metadata": self.__join_tags_and_metadata(tags, metadata),
                "model": model_name,
                "model_parameters": self._parse_model_parameters(kwargs),
                "version": self.version,
                "prompt": registered_prompt,
            }

            if parent_run_id in self.runs:
                self.runs[run_id] = self.runs[parent_run_id].generation(**content)
            elif self.root_span is not None and parent_run_id is None:
                self.runs[run_id] = self.root_span.generation(**content)
            else:
                self.runs[run_id] = self.trace.generation(**content)

        except Exception as e:
            self.log.exception(e)

    @staticmethod
    def _parse_model_parameters(kwargs):
        """Parse the model parameters from the kwargs."""
        if kwargs["invocation_params"].get("_type") == "IBM watsonx.ai" and kwargs[
            "invocation_params"
        ].get("params"):
            kwargs["invocation_params"] = {
                **kwargs["invocation_params"],
                **kwargs["invocation_params"]["params"],
            }
            del kwargs["invocation_params"]["params"]
        return {
            key: value
            for key, value in {
                "temperature": kwargs["invocation_params"].get("temperature"),
                "max_tokens": kwargs["invocation_params"].get("max_tokens"),
                "max_completion_tokens": kwargs["invocation_params"].get(
                    "max_completion_tokens"
                ),
                "top_p": kwargs["invocation_params"].get("top_p"),
                "frequency_penalty": kwargs["invocation_params"].get(
                    "frequency_penalty"
                ),
                "presence_penalty": kwargs["invocation_params"].get("presence_penalty"),
                "request_timeout": kwargs["invocation_params"].get("request_timeout"),
                "decoding_method": kwargs["invocation_params"].get("decoding_method"),
                "min_new_tokens": kwargs["invocation_params"].get("min_new_tokens"),
                "max_new_tokens": kwargs["invocation_params"].get("max_new_tokens"),
                "stop_sequences": kwargs["invocation_params"].get("stop_sequences"),
            }.items()
            if value is not None
        }

    def _parse_model_and_log_errors(self, *, serialized, metadata, kwargs):
        """Parse the model name and log errors if parsing fails."""
        try:
            model_name = _parse_model_name_from_metadata(
                metadata
            ) or _extract_model_name(serialized, **kwargs)

            if model_name:
                return model_name

        except Exception as e:
            self.log.exception(e)
            self._report_error(
                {
                    "log": "unable to parse model name",
                    "kwargs": str(kwargs),
                    "serialized": str(serialized),
                    "exception": str(e),
                }
            )

        self._log_model_parse_warning()

    def _log_model_parse_warning(self):
        if not hasattr(self, "_model_parse_warning_logged"):
            self.log.warning(
                "Langfuse was not able to parse the LLM model. The LLM call will be recorded without model name. Please create an issue: https://github.com/langfuse/langfuse/issues/new/choose"
            )

            self._model_parse_warning_logged = True

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event(
                "on_llm_end", run_id, parent_run_id, response=response, kwargs=kwargs
            )
            if run_id not in self.runs:
                raise Exception("Run not found, see docs what to do in this case.")
            else:
                generation = response.generations[-1][-1]
                extracted_response = (
                    self._convert_message_to_dict(generation.message)
                    if isinstance(generation, ChatGeneration)
                    else _extract_raw_response(generation)
                )

                llm_usage = _parse_usage(response)

                # e.g. azure returns the model name in the response
                model = _parse_model(response)
                self.runs[run_id] = self.runs[run_id].end(
                    output=extracted_response,
                    usage=llm_usage,
                    usage_details=llm_usage,
                    version=self.version,
                    input=kwargs.get("inputs"),
                    model=model,
                )

                self._update_trace_and_remove_state(
                    run_id, parent_run_id, extracted_response
                )

        except Exception as e:
            self.log.exception(e)

        finally:
            self.updated_completion_start_time_memo.discard(run_id)

    def on_llm_error(
        self,
        error: Union[Exception, KeyboardInterrupt],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        try:
            self._log_debug_event("on_llm_error", run_id, parent_run_id, error=error)
            if run_id in self.runs:
                self.runs[run_id] = self.runs[run_id].end(
                    status_message=str(error),
                    level="ERROR",
                    version=self.version,
                    input=kwargs.get("inputs"),
                )
                self._update_trace_and_remove_state(run_id, parent_run_id, error)

        except Exception as e:
            self.log.exception(e)

    def __join_tags_and_metadata(
        self,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        trace_metadata: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        final_dict = {}
        if tags is not None and len(tags) > 0:
            final_dict["tags"] = tags
        if metadata is not None:
            final_dict.update(metadata)
        if trace_metadata is not None:
            final_dict.update(trace_metadata)
        return _strip_langfuse_keys_from_dict(final_dict) if final_dict != {} else None

    def _report_error(self, error: dict):
        event = SdkLogBody(log=error)

        self._task_manager.add_task(
            {
                "id": str(uuid4()),
                "type": "sdk-log",
                "timestamp": _get_timestamp(),
                "body": event.dict(),
            }
        )

    def _update_trace_and_remove_state(
        self,
        run_id: str,
        parent_run_id: Optional[str],
        output: any,
        *,
        keep_state: bool = False,
        **kwargs: Any,
    ):
        """Update the trace with the output of the current run. Called at every finish callback event."""
        chain_trace_updates = self.trace_updates.pop(run_id, {})

        if (
            parent_run_id
            is None  # If we are at the root of the langchain execution -> reached the end of the root
            and self.trace is not None  # We do have a trace available
            and self.trace.id
            == str(run_id)  # The trace was generated by langchain and not by the user
        ):
            self.trace = self.trace.update(
                output=output, **chain_trace_updates, **kwargs
            )

        elif (
            parent_run_id is None
            and self.trace is not None  # We have a user-provided parent
            and self.update_stateful_client
        ):
            if self.root_span is not None:
                self.root_span = self.root_span.update(
                    output=output, **kwargs
                )  # No trace updates if root_span was user provided
            else:
                self.trace = self.trace.update(
                    output=output, **chain_trace_updates, **kwargs
                )

        elif parent_run_id is None and self.langfuse is not None:
            """
            For batch runs, self.trace.id == str(run_id) only for the last run
            For the rest of the runs, the trace must be manually updated
            The check for self.langfuse ensures that no stateful client was provided by the user
            """
            self.langfuse.trace(id=str(run_id)).update(
                output=output, **chain_trace_updates, **kwargs
            )

        if not keep_state:
            del self.runs[run_id]

    def _convert_message_to_dict(self, message: BaseMessage) -> Dict[str, Any]:
        # assistant message
        if isinstance(message, HumanMessage):
            message_dict = {"role": "user", "content": message.content}
        elif isinstance(message, AIMessage):
            message_dict = {"role": "assistant", "content": message.content}
        elif isinstance(message, SystemMessage):
            message_dict = {"role": "system", "content": message.content}
        elif isinstance(message, ToolMessage):
            message_dict = {
                "role": "tool",
                "content": message.content,
                "tool_call_id": message.tool_call_id,
            }
        elif isinstance(message, FunctionMessage):
            message_dict = {"role": "function", "content": message.content}
        elif isinstance(message, ChatMessage):
            message_dict = {"role": message.role, "content": message.content}
        else:
            raise ValueError(f"Got unknown type {message}")
        if "name" in message.additional_kwargs:
            message_dict["name"] = message.additional_kwargs["name"]

        if message.additional_kwargs:
            message_dict["additional_kwargs"] = message.additional_kwargs

        return message_dict

    def _create_message_dicts(
        self, messages: List[BaseMessage]
    ) -> List[Dict[str, Any]]:
        return [self._convert_message_to_dict(m) for m in messages]

    def _log_debug_event(
        self,
        event_name: str,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs,
    ):
        self.log.debug(
            f"Event: {event_name}, run_id: {str(run_id)[:5]}, parent_run_id: {str(parent_run_id)[:5]}"
        )


def _extract_raw_response(last_response):
    """Extract the response from the last response of the LLM call."""
    # We return the text of the response if not empty
    if last_response.text is not None and last_response.text.strip() != "":
        return last_response.text.strip()
    elif hasattr(last_response, "message"):
        # Additional kwargs contains the response in case of tool usage
        return last_response.message.additional_kwargs
    else:
        # Not tool usage, some LLM responses can be simply empty
        return ""


def _flatten_comprehension(matrix):
    return [item for row in matrix for item in row]


def _parse_usage_model(usage: typing.Union[pydantic.BaseModel, dict]):
    # maintains a list of key translations. For each key, the usage model is checked
    # and a new object will be created with the new key if the key exists in the usage model
    # All non matched keys will remain on the object.

    if hasattr(usage, "__dict__"):
        usage = usage.__dict__

    conversion_list = [
        # https://pypi.org/project/langchain-anthropic/ (works also for Bedrock-Anthropic)
        ("input_tokens", "input"),
        ("output_tokens", "output"),
        ("total_tokens", "total"),
        # https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count
        ("prompt_token_count", "input"),
        ("candidates_token_count", "output"),
        # Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-cw.html#runtime-cloudwatch-metrics
        ("inputTokenCount", "input"),
        ("outputTokenCount", "output"),
        ("totalTokenCount", "total"),
        # langchain-ibm https://pypi.org/project/langchain-ibm/
        ("input_token_count", "input"),
        ("generated_token_count", "output"),
    ]

    usage_model = usage.copy()  # Copy all existing key-value pairs

    # Skip OpenAI usage types as they are handled server side
    if not all(
        openai_key in usage_model
        for openai_key in ["prompt_tokens", "completion_tokens", "total_tokens"]
    ):
        for model_key, langfuse_key in conversion_list:
            if model_key in usage_model:
                captured_count = usage_model.pop(model_key)
                final_count = (
                    sum(captured_count)
                    if isinstance(captured_count, list)
                    else captured_count
                )  # For Bedrock, the token count is a list when streamed

                usage_model[langfuse_key] = (
                    final_count  # Translate key and keep the value
                )

    if isinstance(usage_model, dict):
        if "input_token_details" in usage_model:
            input_token_details = usage_model.pop("input_token_details", {})

            for key, value in input_token_details.items():
                usage_model[f"input_{key}"] = value

                if "input" in usage_model:
                    usage_model["input"] = max(0, usage_model["input"] - value)

        if "output_token_details" in usage_model:
            output_token_details = usage_model.pop("output_token_details", {})

            for key, value in output_token_details.items():
                usage_model[f"output_{key}"] = value

                if "output" in usage_model:
                    usage_model["output"] = max(0, usage_model["output"] - value)

        # Vertex AI
        if "prompt_tokens_details" in usage_model and isinstance(
            usage_model["prompt_tokens_details"], list
        ):
            prompt_tokens_details = usage_model.pop("prompt_tokens_details")

            for item in prompt_tokens_details:
                if (
                    isinstance(item, dict)
                    and "modality" in item
                    and "token_count" in item
                ):
                    value = item["token_count"]
                    usage_model[f"input_modality_{item['modality']}"] = value

                    if "input" in usage_model:
                        usage_model["input"] = max(0, usage_model["input"] - value)

        # Vertex AI
        if "candidates_tokens_details" in usage_model and isinstance(
            usage_model["candidates_tokens_details"], list
        ):
            candidates_tokens_details = usage_model.pop("candidates_tokens_details")

            for item in candidates_tokens_details:
                if (
                    isinstance(item, dict)
                    and "modality" in item
                    and "token_count" in item
                ):
                    value = item["token_count"]
                    usage_model[f"output_modality_{item['modality']}"] = value

                    if "output" in usage_model:
                        usage_model["output"] = max(0, usage_model["output"] - value)

        # Vertex AI
        if "cache_tokens_details" in usage_model and isinstance(
            usage_model["cache_tokens_details"], list
        ):
            cache_tokens_details = usage_model.pop("cache_tokens_details")

            for item in cache_tokens_details:
                if (
                    isinstance(item, dict)
                    and "modality" in item
                    and "token_count" in item
                ):
                    value = item["token_count"]
                    usage_model[f"cached_modality_{item['modality']}"] = value

                    if "input" in usage_model:
                        usage_model["input"] = max(0, usage_model["input"] - value)

    usage_model = (
        {
            k: v
            for k, v in usage_model.items()
            if v is not None and not isinstance(v, str)
        }
        if isinstance(usage_model, dict)
        else usage_model
    )

    return usage_model if usage_model else None


def _parse_usage(response: LLMResult):
    # langchain-anthropic uses the usage field
    llm_usage_keys = ["token_usage", "usage"]
    llm_usage = None
    if response.llm_output is not None:
        for key in llm_usage_keys:
            if key in response.llm_output and response.llm_output[key]:
                llm_usage = _parse_usage_model(response.llm_output[key])
                break

    if hasattr(response, "generations"):
        for generation in response.generations:
            for generation_chunk in generation:
                if generation_chunk.generation_info and (
                    "usage_metadata" in generation_chunk.generation_info
                ):
                    llm_usage = _parse_usage_model(
                        generation_chunk.generation_info["usage_metadata"]
                    )
                    break

                message_chunk = getattr(generation_chunk, "message", {})
                response_metadata = getattr(message_chunk, "response_metadata", {})

                chunk_usage = (
                    (
                        response_metadata.get("usage", None)  # for Bedrock-Anthropic
                        if isinstance(response_metadata, dict)
                        else None
                    )
                    or (
                        response_metadata.get(
                            "amazon-bedrock-invocationMetrics", None
                        )  # for Bedrock-Titan
                        if isinstance(response_metadata, dict)
                        else None
                    )
                    or getattr(message_chunk, "usage_metadata", None)  # for Ollama
                )

                if chunk_usage:
                    llm_usage = _parse_usage_model(chunk_usage)
                    break

    return llm_usage


def _parse_model(response: LLMResult):
    # langchain-anthropic uses the usage field
    llm_model_keys = ["model_name"]
    llm_model = None
    if response.llm_output is not None:
        for key in llm_model_keys:
            if key in response.llm_output and response.llm_output[key]:
                llm_model = response.llm_output[key]
                break

    return llm_model


def _parse_model_name_from_metadata(metadata: Optional[Dict[str, Any]]):
    if metadata is None or not isinstance(metadata, dict):
        return None

    return metadata.get("ls_model_name", None)


def _strip_langfuse_keys_from_dict(metadata: Optional[Dict[str, Any]]):
    if metadata is None or not isinstance(metadata, dict):
        return metadata

    langfuse_metadata_keys = [
        "langfuse_prompt",
        "langfuse_session_id",
        "langfuse_user_id",
    ]

    metadata_copy = metadata.copy()

    for key in langfuse_metadata_keys:
        metadata_copy.pop(key, None)

    return metadata_copy
