from pydantic import root_validator
from sqlmodel import SQLModel


class Base(SQLModel):
    @root_validator(pre=True)
    def validate(cls, values):
        for k, v in values.items():
            if isinstance(v, int) and (v < 1) and ("id" in k):
                raise ValueError(f"'{k}' cannot be less than 1 (given {v})")
            elif isinstance(v, str):
                s = v.strip()
                if not s:
                    raise ValueError(f"'{k}' cannot be empty")
                values[k] = s
        return values
