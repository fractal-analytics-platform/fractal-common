from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from ._validators import valstr

__all__ = (
    "_ApplyWorkflowBase",
    "ApplyWorkflowCreate",
    "ApplyWorkflowRead",
)


class _ApplyWorkflowBase(BaseModel):
    """
    Base class for ApplyWorkflow

    Attributes:
        worker_init: TBD
    """

    worker_init: Optional[str]


class ApplyWorkflowCreate(_ApplyWorkflowBase):

    # Validators
    _worker_init = validator("worker_init", allow_reuse=True)(
        valstr("worker_init")
    )


class ApplyWorkflowRead(_ApplyWorkflowBase):
    id: int
    project_id: int
    workflow_id: int
    input_dataset_id: int
    output_dataset_id: int
    start_timestamp: datetime
    end_timestamp: Optional[datetime]
    status: str
    log: Optional[str]
    history: Optional[list[str]]
    working_dir: Optional[str]
    working_dir_user: Optional[str]

    def sanitised_dict(self):
        d = self.dict()
        d["start_timestamp"] = str(self.start_timestamp)
        d["end_timestamp"] = str(self.end_timestamp)
        return d
