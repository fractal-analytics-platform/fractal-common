def valstr(attribute: str):
    """
    Check that a string attribute is not an empty string, and remove the
    leading and trailing whitespace characters.
    """

    def val(string: str):
        if string is None:
            raise ValueError(f"String attribute '{attribute}' cannot be None")
        s = string.strip()
        if not s:
            raise ValueError(f"String attribute '{attribute}' cannot be empty")
        return s

    return val


def valint(attribute: str, min_val: int = 1):
    """
    Check that an integer attribute (e.g. if it is meant to be the ID of a
    database entry) is greater or equal to min_val.
    """

    def val(integer: int):
        if integer is None:
            raise ValueError(f"Integer attribute '{attribute}' cannot be None")
        if integer < min_val:
            raise ValueError(
                f"Integer attribute '{attribute}' cannot be less than "
                f"{min_val} (given {integer})"
            )
        return integer

    return val
