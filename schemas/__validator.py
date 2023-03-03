def validate_str(string, attrname):
    s = string.strip()
    if not s:
        raise ValueError(f"'{attrname}' cannot be empty")
    return s
