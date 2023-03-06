from devtools import debug

from schemas import DatasetRead
from schemas import ResourceRead


def test_dataset_read():
    dsread = DatasetRead(id=1, project_id=1, resource_list=[], name="n")
    debug(dsread)
    rs = ResourceRead(id=1, dataset_id=1, path="/something")
    debug(rs)
    # The following statement fails
    # dsread = DatasetRead(id=1, project_id=1, resource_list=[rs], name="n")


# debug(dsread)
