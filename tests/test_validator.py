import pytest
from config_parser.validator import validate_names

def test_validate_names_correct():
    validate_names("valid_name")  # Не должно выбрасывать исключение

def test_validate_names_invalid():
    with pytest.raises(ValueError, match="Неверное имя:"):
        validate_names("1invalid")

    with pytest.raises(ValueError, match="Неверное имя:"):
        validate_names("invalid-name")

    with pytest.raises(ValueError, match="Неверное имя:"):
        validate_names("")
