from datetime import datetime
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from ._validators import valstr

__all__ = (
    "ApplyWorkflowBase",
    "ApplyWorkflowCreate",
    "ApplyWorkflowRead",
)


class ApplyWorkflowBase(SQLModel):
    """
    Base class for ApplyWorkflow

    Attributes:
        overwrite_input: TBD
        worker_init: TBD
    """

    overwrite_input: bool = False
    worker_init: Optional[str]


class ApplyWorkflowCreate(ApplyWorkflowBase):

    # Validators
    _worker_init = validator("worker_init", allow_reuse=True)(
        valstr("worker_init")
    )


class ApplyWorkflowRead(ApplyWorkflowBase):
    id: int
    start_timestamp: datetime
    status: str
    log: Optional[str]
    history: Optional[List[str]]
    working_dir: Optional[str]
    working_dir_user: Optional[str]

    def sanitised_dict(self):
        d = self.dict()
        d["start_timestamp"] = str(self.start_timestamp)
        return d
