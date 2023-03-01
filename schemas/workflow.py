from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

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
    order: Optional[int]
    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskCreate(_WorkflowTaskBase):
    task_id: int
    workflow_id: Optional[int]

    @validator("task_id", "workflow_id")
    def positive(cls, _id):
        if (_id is not None) and _id < 1:
            raise ValueError(f"IDs must be positive integers, given {_id}")
        return _id


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

    @validator("project_id")
    def positive(cls, _id):
        if _id < 1:
            raise ValueError(f"IDs must be positive integers, given {_id}")
        return _id


class WorkflowUpdate(_WorkflowBase):
    name: Optional[str]  # type: ignore

    @validator("name")
    def not_empty_str(cls, value):
        v = value.strip()
        if not v:
            raise ValueError("'name' cannot be empty")
        else:
            return v


class WorkflowImport(_WorkflowBase):
    task_list: List[WorkflowTaskImport]


class WorkflowExport(_WorkflowBase):
    task_list: List[WorkflowTaskExport]
