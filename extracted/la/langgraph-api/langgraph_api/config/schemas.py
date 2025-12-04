from typing import Literal

from typing_extensions import TypedDict

__all__ = [
    "CheckpointerConfig",
    "ConfigurableHeaders",
    "CorsConfig",
    "HttpConfig",
    "IndexConfig",
    "MiddlewareOrders",
    "SecurityConfig",
    "SerdeConfig",
    "StoreConfig",
    "TTLConfig",
    "ThreadTTLConfig",
]


class CorsConfig(TypedDict, total=False):
    allow_origins: list[str]
    allow_methods: list[str]
    allow_headers: list[str]
    allow_credentials: bool
    allow_origin_regex: str
    expose_headers: list[str]
    max_age: int


class ConfigurableHeaders(TypedDict, total=False):
    includes: list[str] | None
    excludes: list[str] | None
    include: list[str] | None
    exclude: list[str] | None


MiddlewareOrders = Literal["auth_first", "middleware_first"]


class HttpConfig(TypedDict, total=False):
    app: str
    """Import path for a custom Starlette/FastAPI app to mount"""
    disable_assistants: bool
    """Disable /assistants routes"""
    disable_threads: bool
    """Disable /threads routes"""
    disable_runs: bool
    """Disable /runs routes"""
    disable_store: bool
    """Disable /store routes"""
    disable_meta: bool
    """Disable /ok, /info, /metrics, and /docs routes"""
    disable_webhooks: bool
    """Disable webhooks calls on run completion in all routes"""
    cors: CorsConfig | None
    """CORS configuration"""
    disable_ui: bool
    """Disable /ui routes"""
    disable_mcp: bool
    """Disable /mcp routes"""
    mount_prefix: str
    """Prefix for mounted routes. E.g., "/my-deployment/api"."""
    configurable_headers: ConfigurableHeaders | None
    logging_headers: ConfigurableHeaders | None
    enable_custom_route_auth: bool
    middleware_order: MiddlewareOrders | None


class ThreadTTLConfig(TypedDict, total=False):
    strategy: Literal["delete"]
    default_ttl: float | None
    sweep_interval_minutes: int | None


class IndexConfig(TypedDict, total=False):
    """Configuration for indexing documents for semantic search in the store."""

    dims: int
    """Number of dimensions in the embedding vectors.
    
    Common embedding models have the following dimensions:
        - OpenAI text-embedding-3-large: 256, 1024, or 3072
        - OpenAI text-embedding-3-small: 512 or 1536
        - OpenAI text-embedding-ada-002: 1536
        - Cohere embed-english-v3.0: 1024
        - Cohere embed-english-light-v3.0: 384
        - Cohere embed-multilingual-v3.0: 1024
        - Cohere embed-multilingual-light-v3.0: 384
    """

    embed: str
    """Either a path to an embedding model (./path/to/file.py:embedding_model)
    or a name of an embedding model (openai:text-embedding-3-small)
    
    Note: LangChain is required to use the model format specification.
    """

    fields: list[str] | None
    """Fields to extract text from for embedding generation.
    
    Defaults to the root ["$"], which embeds the json object as a whole.
    """


class TTLConfig(TypedDict, total=False):
    """Configuration for TTL (time-to-live) behavior in the store."""

    refresh_on_read: bool
    """Default behavior for refreshing TTLs on read operations (GET and SEARCH).
    
    If True, TTLs will be refreshed on read operations (get/search) by default.
    This can be overridden per-operation by explicitly setting refresh_ttl.
    Defaults to True if not configured.
    """
    default_ttl: float | None
    """Default TTL (time-to-live) in minutes for new items.
    
    If provided, new items will expire after this many minutes after their last access.
    The expiration timer refreshes on both read and write operations.
    Defaults to None (no expiration).
    """
    sweep_interval_minutes: int | None
    """Interval in minutes between TTL sweep operations.
    
    If provided, the store will periodically delete expired items based on TTL.
    Defaults to None (no sweeping).
    """


class StoreConfig(TypedDict, total=False):
    path: str
    index: IndexConfig
    ttl: TTLConfig


class SerdeConfig(TypedDict, total=False):
    """Configuration for the built-in serde, which handles checkpointing of state.

    If omitted, no serde is set up (the object store will still be present, however)."""

    allowed_json_modules: list[list[str]] | Literal[True] | None
    """Optional. List of allowed python modules to de-serialize custom objects from.
    
    If provided, only the specified modules will be allowed to be deserialized.
    If omitted, no modules are allowed, and the object returned will simply be a json object OR
    a deserialized langchain object.
    
    Example:
    {...
        "serde": {
            "allowed_json_modules": [
                ["my_agent", "my_file", "SomeType"],
            ]
        }
    }

    If you set this to True, any module will be allowed to be deserialized.

    Example:
    {...
        "serde": {
            "allowed_json_modules": true
        }
    }
    
    """
    pickle_fallback: bool
    """Optional. Whether to allow pickling as a fallback for deserialization.
    
    If True, pickling will be allowed as a fallback for deserialization.
    If False, pickling will not be allowed as a fallback for deserialization.
    Defaults to True if not configured."""


class CheckpointerConfig(TypedDict, total=False):
    """Configuration for the built-in checkpointer, which handles checkpointing of state.

    If omitted, no checkpointer is set up (the object store will still be present, however).
    """

    ttl: ThreadTTLConfig | None
    """Optional. Defines the TTL (time-to-live) behavior configuration.
    
    If provided, the checkpointer will apply TTL settings according to the configuration.
    If omitted, no TTL behavior is configured.
    """
    serde: SerdeConfig | None
    """Optional. Defines the configuration for how checkpoints are serialized."""


class SecurityConfig(TypedDict, total=False):
    securitySchemes: dict
    security: list
    # path => {method => security}
    paths: dict[str, dict[str, list]]


class CacheConfig(TypedDict, total=False):
    cache_keys: list[str]
    ttl_seconds: int
    max_size: int


class AuthConfig(TypedDict, total=False):
    path: str
    """Path to the authentication function in a Python file."""
    disable_studio_auth: bool
    """Whether to disable auth when connecting from the LangSmith Studio."""
    openapi: SecurityConfig
    """The schema to use for updating the openapi spec.

    Example:
        {
            "securitySchemes": {
                "OAuth2": {
                    "type": "oauth2",
                    "flows": {
                        "password": {
                            "tokenUrl": "/token",
                            "scopes": {
                                "me": "Read information about the current user",
                                "items": "Access to create and manage items"
                            }
                        }
                    }
                }
            },
            "security": [
                {"OAuth2": ["me"]}  # Default security requirement for all endpoints
            ]
        }
    """
    cache: CacheConfig | None
