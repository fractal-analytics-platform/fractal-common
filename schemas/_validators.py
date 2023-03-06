def valstr(attribute: str):
    """
    Check that a string attribute is not an empty string, and remove the
    leading and trailing whitespace characters.
    """

    def val(string: str):
        s = string.strip()
        if not s:
            raise ValueError(f"String attribute '{attribute}' cannot be empty")
        return s

    return val


def valint(attribute: str):
    """
    Check that an integer attribute (meant to be the ID of a database entry) is
    greater or equal to 1.
    """

    def val(integer: int):
        if integer < 1:
            raise ValueError(
                f"Integer attribute '{attribute}' cannot be less than 1 "
                f"(given {integer})"
            )
        return integer

    return val
