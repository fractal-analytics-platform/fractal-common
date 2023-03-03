from datetime import datetime
from typing import List
from typing import Optional

from pydantic import root_validator
from sqlmodel import SQLModel

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

    @root_validator(pre=True)
    def positive_integers(cls, values):
        for k, v in values.items():
            if isinstance(v, int) and (v < 1):
                raise ValueError(f"'{k}' cannot be less than 1 (given {v})")
        return values


class ApplyWorkflowCreate(ApplyWorkflowBase):
    pass


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
