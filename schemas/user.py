import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import validator

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
        s = value.strip()
        if not s:
            raise ValueError("'slurm_user' cannot be empty")
        return s
