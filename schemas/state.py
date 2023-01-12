from datetime import datetime
from typing import Any
from typing import Dict
from typing import Optional

from sqlmodel import SQLModel

__all__ = (
    "_StateBase",
    "StateRead",
)


class _StateBase(SQLModel):
    """
    Base class for `State`

    Attributes:
        id: Primary key
        data: Content of the state
        timestamp: Time stamp of the state
    """
    id: Optional[int]
    data: Dict[str, Any]
    timestamp: datetime

    class Config:
        arbitrary_types_allowed = True

    def sanitised_dict(self):
        """
        Return `self.dict()` after casting `self.timestamp` to a string
        """
        d = self.dict()
        d["timestamp"] = str(self.timestamp)
        return d


class StateRead(_StateBase):
    pass
