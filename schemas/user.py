import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import validator

from schemas.__validator import validate_str

__all__ = (
    "UserRead",
    "UserUpdate",
    "UserCreate",
)


class UserRead(schemas.BaseUser[uuid.UUID]):
    slurm_user: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    slurm_user: Optional[str]


class UserCreate(schemas.BaseUserCreate):
    slurm_user: Optional[str]

    @validator("slurm_user")
    def not_empty_str(cls, value):
        v = validate_str(value, "slurm_user")
        return v
