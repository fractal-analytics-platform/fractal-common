from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import validator

from ._validators import valstr

__all__ = (
    "TaskCreate",
    "TaskUpdate",
    "TaskRead",
    "TaskImport",
    "TaskExport",
)


class _TaskBase(BaseModel):
    """

    # TODO fix me

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
        default_args: Optional[dict[str, Any]]
            dictionary (saved as JSON) of the default parameters of the task
    """

    source: str
    _source = validator("source", allow_reuse=True)(valstr("source"))


class TaskUpdate(_TaskBase):
    name: Optional[str]
    input_type: Optional[str]
    output_type: Optional[str]
    command: Optional[str]
    source: Optional[str]
    default_args: Optional[dict[str, Any]]
    meta: Optional[dict[str, Any]]
    version: Optional[str]
    args_schema: Optional[dict[str, Any]]
    args_schema_version: Optional[str]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _input_type = validator("input_type", allow_reuse=True)(
        valstr("input_type")
    )
    _output_type = validator("output_type", allow_reuse=True)(
        valstr("output_type")
    )
    _command = validator("command", allow_reuse=True)(valstr("command"))
    _version = validator("version", allow_reuse=True)(valstr("version"))


class TaskImport(_TaskBase):
    pass


class TaskExport(_TaskBase):
    pass


class TaskRead(_TaskBase):
    id: int
    name: str
    command: str
    input_type: str
    output_type: str
    default_args: Optional[dict[str, Any]] = Field(default={})
    meta: Optional[dict[str, Any]] = Field(default={})
    owner: Optional[str]
    version: Optional[str]
    args_schema: Optional[dict[str, Any]]
    args_schema_version: Optional[str]


class TaskCreate(_TaskBase):
    name: str
    command: str
    input_type: str
    output_type: str
    default_args: Optional[dict[str, Any]] = Field(default={})
    meta: Optional[dict[str, Any]] = Field(default={})
    version: Optional[str]
    args_schema: Optional[dict[str, Any]]
    args_schema_version: Optional[str]

    # Validators
    _name = validator("name", allow_reuse=True)(valstr("name"))
    _input_type = validator("input_type", allow_reuse=True)(
        valstr("input_type")
    )
    _output_type = validator("output_type", allow_reuse=True)(
        valstr("output_type")
    )
    _command = validator("command", allow_reuse=True)(valstr("command"))
    _version = validator("version", allow_reuse=True)(valstr("version"))
    _args_schema_version = validator("args_schema_version", allow_reuse=True)(
        valstr("args_schema_version")
    )
