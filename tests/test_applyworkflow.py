from devtools import debug

from schemas import ApplyWorkflowCreate


def test_apply_workflow_create():
    # Valid ApplyWorkflowCreate instance / without output_dataset_id
    valid_args = dict(
        overwrite_input=True,
        worker_init="WORKER INIT",
    )
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)
    assert job.output_dataset_id is None
