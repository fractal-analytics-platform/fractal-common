from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import validator
from sqlmodel import Field  # type: ignore
from sqlmodel import SQLModel


__all__ = (
    "TaskCreate",
    "TaskUpdate",
    "TaskRead",
    "TaskCollectPip",
    "TaskCollectStatus",
)


class _TaskBase(SQLModel):
    """
    Task base class

    A Task is the elemental unit of a workflow, and must be a self-standing
    executable.

    Attributes
        name:
            A human readable name for the task
        command:
            The command(s) that executes the task
        source:
            Path or url to task source. This is the information is used to
            match tasks across fractal installations when a workflow is
            imported.
        input_type:
            The type of data the task expects as input
        output_type:
            The type of data the task expects as output
        default_args: Optional[Dict[str, Any]]
            Dictionary (saved as JSON) of the default parameters of the task
    """

    name: str
    command: str
    source: str
    input_type: str
    output_type: str
    default_args: Optional[Dict[str, Any]] = Field(default={})
    meta: Optional[Dict[str, Any]] = Field(default={})

    class Config:
        arbitrary_types_allowed = True


class TaskUpdate(_TaskBase):
    name: Optional[str]  # type:ignore
    input_type: Optional[str]  # type:ignore
    output_type: Optional[str]  # type:ignore
    command: Optional[str]  # type:ignore
    source: Optional[str]  # type:ignore
    default_args: Optional[Dict[str, Any]]  # type:ignore
    meta: Optional[Dict[str, Any]]  # type:ignore


class TaskRead(_TaskBase):
    id: int


class TaskCreate(_TaskBase):
    pass


class _TaskCollectBase(BaseModel):
    pass


class TaskCollectPip(_TaskCollectBase):
    """
    TaskCollectPip class

    Attributes:
        package: TBD
        version: TBD
        python_version: TBD
        package_extras: TBD
    """
    package: str
    version: Optional[str]
    python_version: Optional[str] = None
    package_extras: Optional[str]

    @validator("package")
    def package_path_absolute(cls, value):
        if "/" in value:
            package_path = Path(value)
            if not package_path.is_absolute():
                raise ValueError(
                    f"Package path must be absolute: {package_path}"
                )
            if not package_path.exists():
                raise ValueError(
                    f"Package file does not exist: {package_path}"
                )
        return value


class TaskCollectStatus(_TaskCollectBase):
    """
    TaskCollectStatus class
    
    Attributes:
        status: TBD
        package: TBD
        venv_path: TBD
        task_list: TBD
        log: TBD
        info: TBD
    """

    status: Literal["pending", "installing", "collecting", "fail", "OK"]
    package: str
    venv_path: Path
    task_list: Optional[List[TaskRead]] = Field(default=[])
    log: Optional[str]
    info: Optional[str]

    def sanitised_dict(self):
        """
        Return `self.dict()` after casting `self.venv_path` to a string
        """
        d = self.dict()
        d["venv_path"] = str(self.venv_path)
        return d
