from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from .task import TaskExport
from .task import TaskImport
from .task import TaskRead
from .validator import valint
from .validator import valstr


__all__ = (
    "WorkflowCreate",
    "WorkflowRead",
    "WorkflowUpdate",
    "WorkflowImport",
    "WorkflowExport",
    "WorkflowTaskCreate",
    "WorkflowTaskImport",
    "WorkflowTaskExport",
    "WorkflowTaskRead",
    "WorkflowTaskUpdate",
)


class _WorkflowTaskBase(SQLModel):
    order: Optional[int]
    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskCreate(_WorkflowTaskBase):
    task_id: int
    workflow_id: Optional[int]

    # Validators
    _order = validator("order", allow_reuse=True)(valint("order"))
    _task_id = validator("task_id", allow_reuse=True)(valint("task_id"))
    _workflow_id = validator("workflow_id", allow_reuse=True)(
        valint("workflow_id")
    )


class WorkflowTaskRead(_WorkflowTaskBase):
    id: int
    workflow_id: int
    task_id: int
    task: TaskRead


class WorkflowTaskImport(_WorkflowTaskBase):
    task: TaskImport


class WorkflowTaskExport(_WorkflowTaskBase):
    task: TaskExport


class WorkflowTaskUpdate(_WorkflowTaskBase):
    # Validators
    _order = validator("order", allow_reuse=True)(valint("order"))
    _task_id = validator("task_id", allow_reuse=True)(valint("task_id"))
    _workflow_id = validator("workflow_id", allow_reuse=True)(
        valint("workflow_id")
    )

    @validator("meta")
    def check_no_parallelisation_level(cls, m):
        if "parallelization_level" in m:
            raise ValueError(
                "Overriding task parallelization level currently not allowed"
            )
        return m


class _WorkflowBase(SQLModel):
    name: str


class WorkflowRead(_WorkflowBase):
    id: int
    project_id: int
    task_list: List[WorkflowTaskRead]


class WorkflowCreate(_WorkflowBase):
    project_id: int

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _project_id = validator("project_id", allow_reuse=True)(
        valint("project_id")
    )


class WorkflowUpdate(_WorkflowBase):
    name: Optional[str]  # type: ignore

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _project_id = validator("project_id", allow_reuse=True)(
        valint("project_id")
    )


class WorkflowImport(_WorkflowBase):
    task_list: List[WorkflowTaskImport]


class WorkflowExport(_WorkflowBase):
    task_list: List[WorkflowTaskExport]
