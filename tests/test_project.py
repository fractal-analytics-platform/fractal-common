import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import ProjectCreate


def test_project_create():
    # Successful creation
    p = ProjectCreate(name="my project", project_dir="/somewhere")
    debug(p)
    # Check that whitespaces are stripped from beginning/end of string
    NAME = "some project name"
    p = ProjectCreate(name=f"  {NAME}  ", project_dir="/somewhere")
    debug(p)
    assert p.name == NAME
    # Fail due to empty strings
    with pytest.raises(ValidationError):
        ProjectCreate(name="  ", project_dir="/somewhere")

    with pytest.raises(ValidationError):
        ProjectCreate(name="my project", project_dir=" ")
