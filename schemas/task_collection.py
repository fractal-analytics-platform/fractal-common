from pathlib import Path
from typing import Literal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from .task import TaskRead

__all__ = (
    "TaskCollectPip",
    "TaskCollectStatus",
)


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
    task_list: Optional[list[TaskRead]] = Field(default=[])
    log: Optional[str]
    info: Optional[str]

    def sanitised_dict(self):
        """
        Return `self.dict()` after casting `self.venv_path` to a string
        """
        d = self.dict()
        d["venv_path"] = str(self.venv_path)
        return d
