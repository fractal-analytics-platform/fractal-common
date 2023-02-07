from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import validator
from sqlmodel import SQLModel

from .task import TaskRead
from .task import TaskImport
from .task import TaskExport


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
    workflow_id: Optional[int]
    task_id: Optional[int]
    order: Optional[int]
    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskCreate(_WorkflowTaskBase):
    task_id: int


class WorkflowTaskRead(_WorkflowTaskBase):
    id: int
    workflow_id: int
    task: TaskRead


class WorkflowTaskImport(_WorkflowTaskBase):
    task: TaskImport


class WorkflowTaskExport(_WorkflowTaskBase):
    task: TaskExport


class WorkflowTaskUpdate(_WorkflowTaskBase):
    args: Optional[Dict[str, Any]]  # type: ignore
    meta: Optional[Dict[str, Any]]  # type: ignore

    @validator("meta")
    def check_no_parallelisation_level(cls, m):
        if "parallelization_level" in m:
            raise ValueError(
                "Overriding task parallelization level currently not allowed"
            )
        return m


class _WorkflowBase(SQLModel):
    name: str
    project_id: int


class WorkflowRead(_WorkflowBase):
    id: int
    task_list: List[WorkflowTaskRead]


class WorkflowCreate(_WorkflowBase):
    pass


class WorkflowImport(_WorkflowBase):
    task_list: List[WorkflowTaskImport]


class WorkflowExport(_WorkflowBase):
    project_id: Optional[int]
    task_list: List[WorkflowTaskExport]


class WorkflowUpdate(_WorkflowBase):
    name: Optional[str]  # type: ignore
    project_id: Optional[int]  # type: ignore
