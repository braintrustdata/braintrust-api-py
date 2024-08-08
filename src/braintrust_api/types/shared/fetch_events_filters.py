# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .path_lookup_filter import PathLookupFilter

__all__ = ["FetchEventsFilters"]

FetchEventsFilters: TypeAlias = List[PathLookupFilter]
