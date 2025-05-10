from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `braintrust_api.resources` module.

    This is used so that we can lazily import `braintrust_api.resources` only when
    needed *and* so that users can just import `braintrust_api` and reference `braintrust_api.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("braintrust_api.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
