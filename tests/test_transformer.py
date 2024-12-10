import pytest
from config_parser.transformer import transform_to_yaml

def test_transform_to_yaml():
    data = {
        "constants": {"x": 10, "y": 20},
        "expressions": [11, 15],
        "lists": [["1", "2", "3"], ["a", "b", "c"]]
    }
    result = transform_to_yaml(data)
    expected_yaml = (
        "constants:\n"
        "  x: 10\n"
        "  y: 20\n"
        "expressions:\n"
        "- 11\n"
        "- 15\n"
        "lists:\n"
        "- - '1'\n"
        "  - '2'\n"
        "  - '3'\n"
        "- - 'a'\n"
        "  - 'b'\n"
        "  - 'c'\n"
    )
    assert result.strip() == expected_yaml.strip()
