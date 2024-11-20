# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .shared.insert_events_response import InsertEventsResponse

__all__ = ["ExperimentInsertResponse"]


class ExperimentInsertResponse(InsertEventsResponse):
    serialized_span_slugs: List[str]
    """String slugs which line up 1-1 with the row_ids.

    These slugs can be used as the 'parent' specifier to attach spans underneath the
    row
    """
