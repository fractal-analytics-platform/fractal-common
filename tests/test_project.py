import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import DatasetCreate
from schemas import DatasetRead
from schemas import ProjectCreate
from schemas import ResourceRead


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


def test_dataset_create():
    # Successful creation
    d = DatasetCreate(name="name")
    # Successful sanification of whitespaces
    NAME = "name"
    d = DatasetCreate(name=f"   {NAME}   ")
    assert d.name == NAME
    # Missing argument
    with pytest.raises(ValidationError):
        d = DatasetCreate()
    # Empty-string argument
    with pytest.raises(ValidationError):
        d = DatasetCreate(name="  ")


def test_dataset_read():
    # Successful creation - empty resource_list
    d = DatasetRead(id=1, project_id=1, resource_list=[], name="n")
    debug(d)
    # Successful creation - non-trivial resource_list
    r1 = ResourceRead(id=1, dataset_id=1, path="/something")
    r2 = ResourceRead(id=1, dataset_id=1, path="/something")
    d = DatasetRead(id=1, project_id=1, resource_list=[r1, r2], name="n")
    debug(d)
