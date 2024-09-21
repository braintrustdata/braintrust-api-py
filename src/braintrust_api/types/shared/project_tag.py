# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectTag"]

class ProjectTag(BaseModel):
    id: str
    """Unique identifier for the project tag"""

    name: str
    """Name of the project tag"""

    project_id: str
    """Unique identifier for the project that the project tag belongs under"""

    user_id: str

    color: Optional[str] = None
    """Color of the tag for the UI"""

    created: Optional[datetime] = None
    """Date of project tag creation"""

    description: Optional[str] = None
    """Textual description of the project tag"""