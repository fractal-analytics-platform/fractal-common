import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import DatasetCreate
from schemas import DatasetRead
from schemas import ResourceRead


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


@pytest.mark.xfail(reason="In-progress")
def test_dataset_read():
    d = DatasetRead(id=1, project_id=1, resource_list=[], name="n")
    debug(d)
    r = ResourceRead(id=1, dataset_id=1, path="/something")
    debug(r)
    # FIXME: The following statement fails
    d2 = DatasetRead(id=1, project_id=1, resource_list=[r], name="n")
    debug(d2)
