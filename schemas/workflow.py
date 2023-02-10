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
    workflow_id: Optional[int]  # FIXME check optional


class WorkflowTaskRead(_WorkflowTaskBase):
    id: int
    workflow_id: int
    task: TaskRead
    task_id: Optional[int]  # FIXME make required


class WorkflowTaskImport(_WorkflowTaskBase):
    task: TaskImport
    order: Optional[int]
    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskExport(_WorkflowTaskBase):
    task: TaskExport
    order: Optional[int]
    meta: Optional[Dict[str, Any]] = None
    args: Optional[Dict[str, Any]] = None


class WorkflowTaskUpdate(_WorkflowTaskBase):
    args: Optional[Dict[str, Any]]  # type: ignore
    meta: Optional[Dict[str, Any]]  # type: ignore
    workflow_id: Optional[int]  # FIXME remove later
    task_id: Optional[int]  # FIXME remove later

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


class WorkflowUpdate(_WorkflowBase):
    name: Optional[str]  # type: ignore
    project_id: Optional[int]  # type: ignore


class WorkflowImport(_WorkflowBase):
    name: str
    task_list: List[WorkflowTaskImport]


class WorkflowExport(_WorkflowBase):
    name: str
    task_list: List[WorkflowTaskExport]
