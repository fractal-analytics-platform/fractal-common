import pytest
from devtools import debug
from pydantic.error_wrappers import ValidationError

from schemas import UserCreate


def test_user_create():
    # Without slurm_user attribute
    u = UserCreate(email="a@b.c", password="asd")
    debug(u)
    assert u.slurm_user is None
    # With valid slurm_user attribute
    u = UserCreate(email="a@b.c", password="asd", slurm_user="slurm_user")
    debug(u)
    assert u.slurm_user
    # With invalid slurm_user attribute
    with pytest.raises(ValidationError):
        u = UserCreate(email="a@b.c", password="asd", slurm_user="  ")
