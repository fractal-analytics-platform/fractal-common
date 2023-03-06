from pydantic import root_validator
from sqlmodel import SQLModel


class ValidatedSQLModel(SQLModel):
    """
    Validates and sanitizes attributes on construction for derived classes.

    - Removes leading and trailing whitespace from strings. If nothing remains
      raises ValueError;
    - Checks that foreign keys are all greater than 1.
    """

    @root_validator(pre=True)
    def validate(cls, values):
        if isinstance(values, dict) is False:
            values = values.dict()
        for k, v in values.items():
            if (
                (k in ["project_id", "workflow_id", "task_id", "dataset_id"])
                and isinstance(v, int)
                and (v < 1)
            ):
                raise ValueError(f"'{k}' cannot be less than 1 (given {v})")
            elif isinstance(v, str):
                s = v.strip()
                if not s:
                    raise ValueError(f"'{k}' cannot be empty")
                values[k] = s
        return values
