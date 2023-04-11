def to_bool(value):
    if isinstance(value, bool):
        # If the value is already a boolean, return it directly
        return value
    elif value.lower() in {'true', 'yes', 'on', '1'}:
        # If the value is a string representing a "true" value, return True
        return True
    elif value.lower() in {'false', 'no', 'off', '0'}:
        # If the value is a string representing a "false" value, return False
        return False
    else:
        # If the value is not a boolean or a string representing a boolean value, raise an error
        raise ValueError("Invalid boolean value: {}".format(value))
