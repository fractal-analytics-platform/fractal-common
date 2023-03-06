import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import TaskCreate
from schemas import TaskUpdate


def test_task_update():
    # Successful creation, with many unset fields
    t = TaskUpdate(name="name")
    debug(t)
    assert list(t.dict(exclude_none=True).keys()) == ["name"]
    assert list(t.dict(exclude_unset=True).keys()) == ["name"]


def test_task_create():
    # Successful creation
    t = TaskCreate(
        name="task",
        source="source",
        command="command",
        input_type="input_type",
        output_type="output_type",
    )
    debug(t)
    # Missing arguments
    with pytest.raises(ValidationError):
        TaskCreate(name="task", source="source")
