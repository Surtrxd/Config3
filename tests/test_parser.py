import pytest
from config_parser.parser import remove_comments, parse_lists, parse_constants, parse_expressions

def test_remove_comments():
    input_text = "#| Это комментарий |# Текст"
    result = remove_comments(input_text)
    assert result.strip() == "Текст"

def test_parse_lists():
    input_text = "list(1 2 3) list(a b c)"
    result = parse_lists(input_text)
    assert result == [["1", "2", "3"], ["a", "b", "c"]]

def test_parse_constants():
    input_text = "(define x 10); (define y 20);"
    result = parse_constants(input_text)
    assert result == {"x": 10, "y": 20}

def test_parse_expressions():
    input_text = "(define x 10); ?[x + 1]"
    constants = parse_constants(input_text)
    result = parse_expressions(input_text, constants)
    assert result == [11]

def test_parse_expressions_with_error():
    input_text = "(define x 10); ?[z + 1]"
    constants = parse_constants(input_text)
    with pytest.raises(ValueError, match="Ошибка в выражении:"):
        parse_expressions(input_text, constants)
