def validate_str(string, attrname):
    """
    Removes leading and trailing whitespace from string.
    If nothing remains raises ValueError, else returns the stripped string.
    """
    s = string.strip()
    if not s:
        raise ValueError(f"'{attrname}' cannot be empty")
    return s
