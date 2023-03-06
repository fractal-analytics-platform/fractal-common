import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import ManifestV1
from schemas import TaskManifestV1


def test_ManifestV1():

    t = TaskManifestV1(
        name="task",
        executable="executable",
        input_type="input_type",
        output_type="output_type",
        default_args={"arg": "val"},
    )
    m = ManifestV1(manifest_version="1", task_list=[t])
    debug(m)

    with pytest.raises(ValidationError):
        ManifestV1(manifest_version="2", task_list=[])
