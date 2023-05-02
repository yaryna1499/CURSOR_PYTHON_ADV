import re


patterns = {
    "[A-Z]": "Please, use at least one capital letter.",
    "[a-z]": "Please, use at least one small letter.",
    "\d": "Please, use at least one digit.",
    "[@$!%*?&_]": "Please, use at least one special symbol.",
    "^.{8}$": "Password should be 8 symbols length.",
    "^\S+$": "Your password contains space characters!",
}


def validator(patterns, password):
    warnings = list()
    for pattern, descr in patterns.items():
        if not re.search(rf"{pattern}", password):
            warnings.append(descr)

    return "\n".join(worning for worning in warnings)


test_string = str(input())

print(validator(patterns, test_string))
