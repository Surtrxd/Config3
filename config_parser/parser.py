import re
from config_parser.validator import validate_names


def remove_comments(input_text):
    return re.sub(r"#\|.*?\|#", "", input_text, flags=re.DOTALL)

def parse_lists(input_text):
    matches = re.finditer(r"list\((.*?)\)", input_text)
    lists = []
    for match in matches:
        elements = match.group(1).split()
        lists.append(elements)
    return lists

def parse_constants(input_text):
    matches = re.findall(r"\(define ([a-zA-Z]+) (\d+)\);", input_text)
    constants = {}
    for name, value in matches:
        validate_names(name)
        constants[name] = int(value)
    return constants

def parse_expressions(input_text, constants):
    matches = re.findall(r"\?\[(.*?)\]", input_text)
    results = []
    for expression in matches:
        try:
            for name, value in constants.items():
                expression = expression.replace(name, str(value))
            result = eval(expression)
            results.append(result)
        except Exception as e:
            raise ValueError(f"Ошибка в выражении: {expression}") from e
    return results
