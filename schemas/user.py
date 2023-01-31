import uuid
from typing import Optional

from fastapi_users import schemas

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
