from devtools import debug

from schemas import ApplyWorkflowCreate


def test_apply_workflow_create():
    # Valid ApplyWorkflowCreate instance
    valid_args = dict(
        overwrite_input=True,
        worker_init="WORKER INIT",
    )
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)
