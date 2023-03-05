from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from pydantic import validator

from .base import Base


__all__ = (
    "ProjectCreate",
    "ProjectRead",
    "DatasetUpdate",
    "DatasetCreate",
    "DatasetRead",
    "ResourceCreate",
    "ResourceRead",
    "ResourceUpdate",
)


class _ProjectBase(Base):
    """
    Base class for Project

    Attributes:
        name: TBD
        project_dir: TBD
        read_only: TBD
    """

    name: str
    project_dir: str
    read_only: bool = False


class ProjectCreate(_ProjectBase):
    default_dataset_name: Optional[str] = "default"

    # TODO test this
    @validator("default_dataset_name")
    def not_null(cls, value):
        """if value.strip()=="" then returns "default"
        else return value.strip()
        """
        return value.strip() or "default"


class ProjectRead(_ProjectBase):
    id: int
    dataset_list: List["DatasetRead"] = []


# DATASET


class _DatasetBase(Base):
    """
    Base class for Dataset

    Attributes:
        name: TBD
        type: TBD
        meta: TBD
        read_only: TBD
    """

    name: str
    type: Optional[str]
    meta: Dict[str, Any] = {}
    read_only: Optional[bool] = False


class DatasetUpdate(_DatasetBase):
    name: Optional[str]  # type:ignore
    meta: Optional[Dict[str, Any]] = None  # type:ignore


class DatasetCreate(_DatasetBase):
    pass


class DatasetRead(_DatasetBase):
    id: int
    resource_list: List["ResourceRead"]
    project_id: Optional[int]


# RESOURCE


class _ResourceBase(Base):
    """
    Base class for Resource
    """

    path: str


class ResourceCreate(_ResourceBase):
    pass


class ResourceUpdate(_ResourceBase):
    pass


class ResourceRead(_ResourceBase):
    id: int
    dataset_id: int


ProjectRead.update_forward_refs()
DatasetRead.update_forward_refs()
