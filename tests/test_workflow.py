import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import TaskRead
from schemas import WorkflowCreate
from schemas import WorkflowRead
from schemas import WorkflowTaskCreate
from schemas import WorkflowTaskRead
from schemas import WorkflowTaskUpdate


def test_workflow_task_create():
    # Successful creation
    t = WorkflowTaskCreate(task_id=1, workflow_id=1)
    debug(t)
    # Missing arguments
    with pytest.raises(ValidationError):
        WorkflowTaskCreate(task_id=1, workflow_id=-1)


def test_workflow_task_update():
    # Success
    t = WorkflowTaskUpdate(meta=dict(something="else"))
    # Failure
    with pytest.raises(ValidationError):
        t = WorkflowTaskUpdate(meta=dict(parallelization_level="new"))
    debug(t)


def test_workflow_create():
    w = WorkflowCreate(name="workflow", project_id=1)
    debug(w)


def test_workflow_read_empty_task_list():
    w = WorkflowRead(id=1, name="workflow", project_id=1, task_list=[])
    debug(w)


def test_workflow_read_non_empty_task_list():
    # Create a TaskRead
    t1 = TaskRead(
        id=9,
        name="name",
        source="source",
        command="command",
        input_type="input_type",
        output_type="output_type",
        meta=dict(something="else"),
    )
    # Create two WorkflowTaskRead
    wft1 = WorkflowTaskRead(id=1, task_id=1, workflow_id=1, task=t1)
    wft2 = WorkflowTaskRead(id=2, task_id=1, workflow_id=1, task=t1)
    # Create a WorkflowRead
    w = WorkflowRead(
        id=1, name="workflow", project_id=1, task_list=[wft1, wft2]
    )
    debug(w)
