from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from ._validators import valint
from ._validators import valstr
from .task import TaskExport
from .task import TaskImport
from .task import TaskRead


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

    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskCreate(_WorkflowTaskBase):
    order: Optional[int]
    task_id: int
    # Validators
    _order = validator("order", allow_reuse=True)(valint("order", min_val=0))
    _task_id = validator("task_id", allow_reuse=True)(valint("task_id"))


class WorkflowTaskRead(_WorkflowTaskBase):
    id: int
    order: Optional[int]
    workflow_id: int
    task_id: int
    task: TaskRead


class WorkflowTaskImport(_WorkflowTaskBase):
    task: TaskImport


class WorkflowTaskExport(_WorkflowTaskBase):
    task: TaskExport


class WorkflowTaskUpdate(_WorkflowTaskBase):
    # Validators
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
    name: Optional[str]
    order_task_list: Optional[List[int]]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))

    @validator("order_task_list")
    def check_permutation(cls, task_list):
        if set(task_list) != set([i for i in range(len(task_list))]):
            raise ValueError(
                "`order_task_list` must be a permutation of "
                f"{[i for i in range(len(task_list))]} (given {task_list})"
            )
        return task_list


class WorkflowImport(_WorkflowBase):
    task_list: List[WorkflowTaskImport]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))


class WorkflowExport(_WorkflowBase):
    task_list: List[WorkflowTaskExport]
