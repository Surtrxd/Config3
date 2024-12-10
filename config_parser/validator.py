import re

def validate_names(name):
    if not re.match(r"^[a-zA-Z]+$", name):
        raise ValueError(f"Неверное имя: {name}")
