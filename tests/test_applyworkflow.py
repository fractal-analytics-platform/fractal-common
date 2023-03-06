import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import ApplyWorkflowCreate


@pytest.mark.xfail(reason="Not implemented yet", strict=True)
def test_apply_workflow_create():
    # Valid ApplyWorkflowCreate instance
    valid_args = dict(
        project_id=1,
        input_dataset_id=1,
        output_dataset_id=2,
        workflow_id=3,
        overwrite_input=True,
        worker_init="WORKER INIT",
    )
    job = ApplyWorkflowCreate(**valid_args)
    debug(job)
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
