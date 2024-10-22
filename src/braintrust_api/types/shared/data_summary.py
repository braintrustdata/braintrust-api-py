# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["DataSummary"]


class DataSummary(BaseModel):
    total_records: int
    """Total number of records in the dataset"""
