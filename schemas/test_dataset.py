from devtools import debug

from . import DatasetRead
from . import ResourceRead


def test_dataset_read():
    dsread = DatasetRead(id=1, project_id=1, resource_list=[], name="n")
    debug(dsread)
    rsread = ResourceRead(id=1, dataset_id=1, path="/something")
    debug(rsread)
    dsread = DatasetRead(id=1, project_id=1, resource_list=[rsread], name="n")
    debug(dsread)
