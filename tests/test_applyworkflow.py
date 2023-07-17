import pytest
from devtools import debug

from schemas import ApplyWorkflowCreate


def test_apply_workflow_create():
    # Valid ApplyWorkflowCreate instance
    valid_args = dict(worker_init="WORKER INIT")
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)

    with pytest.raises(ValueError) as e:
        job = ApplyWorkflowCreate(first_task_index=-1)
    debug(e)

    with pytest.raises(ValueError) as e:
        job = ApplyWorkflowCreate(last_task_index=-1)
    debug(e)

    with pytest.raises(ValueError) as e:
        job = ApplyWorkflowCreate(first_task_index=2, last_task_index=0)
    debug(e)
