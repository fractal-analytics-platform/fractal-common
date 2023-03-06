import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import ApplyWorkflowCreate


def test_apply_workflow_create():
    # Valid ApplyWorkflowCreate instance / without output_dataset_id
    valid_args = dict(
        project_id=1,
        input_dataset_id=1,
        workflow_id=3,
        overwrite_input=True,
        worker_init="WORKER INIT",
    )
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)
    assert job.output_dataset_id is None
    # Valid ApplyWorkflowCreate instance / with output_dataset_id
    valid_args["output_dataset_id"] = 3
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)
    assert job.output_dataset_id
    # Multiple cases of invalid arguments
    for key in [
        "project_id",
        "input_dataset_id",
        "output_dataset_id",
        "workflow_id",
    ]:
        invalid_args = valid_args.copy()
        invalid_args[key] = -1
        debug(invalid_args)
        with pytest.raises(ValidationError):
            ApplyWorkflowCreate(**invalid_args)
