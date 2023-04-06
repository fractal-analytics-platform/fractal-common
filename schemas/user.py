import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import validator

from ._validators import val_absolute_path
from ._validators import valstr


__all__ = (
    "UserRead",
    "UserUpdate",
    "UserCreate",
)


class UserRead(schemas.BaseUser[uuid.UUID]):
    slurm_user: Optional[str]
    cache_dir: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    slurm_user: Optional[str]
    cache_dir: Optional[str]

    # Validators
    _slurm_user = validator("slurm_user", allow_reuse=True)(
        valstr("slurm_user")
    )
    _cache_dir = validator("cache_dir", allow_reuse=True)(
        val_absolute_path("cache_dir")
    )


class UserCreate(schemas.BaseUserCreate):
    slurm_user: Optional[str]
    cache_dir: Optional[str]

    # Validators
    _slurm_user = validator("slurm_user", allow_reuse=True)(
        valstr("slurm_user")
    )
    _cache_dir = validator("cache_dir", allow_reuse=True)(
        val_absolute_path("cache_dir")
    )
