from datetime import datetime
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from ._validators import valint
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
        input_dataset_id: TBD
        output_dataset_id: TBD
        workflow_id: TBD
        overwrite_input: TBD
        worker_init: TBD
        working_dir: TBD
        working_dir_user: TBD
    """

    project_id: int
    input_dataset_id: int
    output_dataset_id: Optional[int]
    workflow_id: int
    overwrite_input: bool = False
    worker_init: Optional[str]


class ApplyWorkflowCreate(ApplyWorkflowBase):

    # Validators
    _project_id = validator("project_id", allow_reuse=True)(
        valint("project_id")
    )
    _input_dataset_id = validator("input_dataset_id", allow_reuse=True)(
        valint("input_dataset_id")
    )
    _output_dataset_id = validator("output_dataset_id", allow_reuse=True)(
        valint("output_dataset_id")
    )
    _workflow_id = validator("workflow_id", allow_reuse=True)(
        valint("workflow_id")
    )
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
