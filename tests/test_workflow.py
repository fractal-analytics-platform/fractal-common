import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import WorkflowCreate
from schemas import WorkflowRead
from schemas import WorkflowTaskCreate
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


@pytest.mark.xfail()
def test_workflow_read():
    # Empty task list
    w = WorkflowRead(id=1, name="workflow", project_id=1, task_list=[])
    debug(w)
    # Non-empty task list
    t1 = WorkflowTaskCreate(task_id=1, workflow_id=1)
    t2 = WorkflowTaskCreate(task_id=1, workflow_id=1)
    w = WorkflowRead(id=1, name="workflow", project_id=1, task_list=[t1, t2])
    debug(w)
