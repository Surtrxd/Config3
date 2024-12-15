import re

def remove_comments(input_text):
    """
    Удаляет многострочные комментарии из текста.
    """
    return re.sub(r"#\|.*?\|#", "", input_text, flags=re.DOTALL)

def parse_lists(input_text):
    """
    Парсит списки, включая вложенные конструкции. Все элементы интерпретируются как строки или числа.
    """
    def parse_nested_list(expression):
        expression = expression.strip()
        if expression.startswith("list(") and expression.endswith(")"):
            inner = expression[5:-1].strip()  # Убираем "list(" и финальную ")"
            stack = []
            buffer = ""
            current_list = []
            for char in inner:
                if char == "(":
                    stack.append(current_list)
                    current_list = []
                elif char == ")":
                    if buffer.strip():
                        current_list.append(parse_nested_list(buffer.strip()))
                        buffer = ""
                    if stack:
                        parent_list = stack.pop()
                        parent_list.append(current_list)
                        current_list = parent_list
                elif char in " \t" and not stack:
                    if buffer.strip():
                        current_list.append(parse_nested_list(buffer.strip()))
                        buffer = ""
                else:
                    buffer += char
            if buffer.strip():
                current_list.append(parse_nested_list(buffer.strip()))
            return current_list
        try:
            return int(expression)
        except ValueError:
            return expression.strip("'").strip('"')

    # Сопоставляем все конструкции list(...)
    # Можно использовать parse_lists для других целей при необходимости.
    matches = re.finditer(r"list\((.*?)\)", input_text)
    lists_ = [parse_nested_list(match.group(0)) for match in matches]
    return lists_

def parse_constants(input_text):
    """
    Парсит константы, определённые с помощью синтаксиса (define имя значение).
    Поддерживает числа и списки.
    Пример: (define x 10);
             (define y (list 1 2 3));
    """
    matches = re.findall(r"\(define\s+([a-zA-Z_]+)\s+(\(.*?\)|\d+)\);", input_text)
    constants = {}
    for name, value in matches:
        value = value.strip()
        if value.startswith("(list"):
            # Конвертируем (list 1 2 3) в [1, 2, 3]
            # Удаляем "(list" и заключительную скобку
            inner = value[5:].strip()[:-1].strip()
            # Разбиваем по пробелам
            items = inner.split()
            # Превращаем в валидный Python-список
            py_list = [int(item) if item.isdigit() else item.strip("'").strip('"') for item in items]
            constants[name] = py_list
        else:
            # Просто число
            constants[name] = int(value)
    return constants

def parse_expressions(input_text, constants):
    """
    Вычисляет арифметические выражения и функции, такие как sort.
    Пример: ?[x + y], ?[sort(example_list)]
    """
    matches = re.findall(r"\?\[(.*?)\]", input_text)
    results = []
    for expression in matches:
        expr = expression.strip()

        # Сначала обрабатываем sort(...)
        sort_match = re.search(r"sort\((.*?)\)", expr)
        if sort_match:
            to_sort = sort_match.group(1).strip()
            if to_sort in constants and isinstance(constants[to_sort], list):
                sorted_list = sorted(constants[to_sort])
                expr = expr.replace(f"sort({to_sort})", str(sorted_list))
            else:
                raise ValueError(f"Переменная '{to_sort}' не определена или не является списком.")

        # Подставляем значения констант
        for name, val in constants.items():
            # \b чтобы избежать частичных совпадений имён
            expr = re.sub(rf"\b{name}\b", str(val), expr)

        # Вычисляем выражение
        result = eval(expr, {"__builtins__": {}}, {})
        results.append(result)
    return results

def preprocess_text(input_text):
    """
    Предварительная обработка текста: удаление комментариев, парсинг констант, списков и выражений.
    Возвращает кортеж (constants, lists, expressions_results).
    """
    no_comments = remove_comments(input_text)
    constants = parse_constants(no_comments)
    lists_ = parse_lists(no_comments)
    expressions = parse_expressions(no_comments, constants)
    return constants, lists_, expressions
