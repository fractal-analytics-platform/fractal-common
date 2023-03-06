def valstr(attribute: str):
    def val(string: str):
        s = string.strip()
        if not s:
            raise ValueError(f"'{attribute}' cannot be empty")
        return s

    return val


def valint(attribute: str):
    def val(integer: int):
        if integer < 1:
            raise ValueError(
                f"'{attribute}' cannot be less than 1 (given {integer})"
            )
        return integer

    return val
