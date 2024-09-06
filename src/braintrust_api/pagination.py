# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncListObjects", "AsyncListObjects"]

_T = TypeVar("_T")


@runtime_checkable
class ListObjectsItem(Protocol):
    id: str


class SyncListObjects(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    """Pagination for endpoints which list data objects"""

    objects: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        objects = self.objects
        if not objects:
            return []
        return objects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        objects = self.objects
        if not objects:
            return None

        if is_forwards:
            item = cast(Any, objects[-1])
            if not isinstance(item, ListObjectsItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.id})
        else:
            item = cast(Any, self.objects[0])
            if not isinstance(item, ListObjectsItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.id})


class AsyncListObjects(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    """Pagination for endpoints which list data objects"""

    objects: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        objects = self.objects
        if not objects:
            return []
        return objects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        objects = self.objects
        if not objects:
            return None

        if is_forwards:
            item = cast(Any, objects[-1])
            if not isinstance(item, ListObjectsItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.id})
        else:
            item = cast(Any, self.objects[0])
            if not isinstance(item, ListObjectsItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.id})
