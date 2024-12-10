import unittest
from config_parser.parser import remove_comments, parse_lists, parse_constants

class TestParser(unittest.TestCase):
    def test_remove_comments(self):
        input_text = "#| Это комментарий |# Текст"
        result = remove_comments(input_text)
        self.assertEqual(result.strip(), "Текст")

    def test_parse_lists(self):
        input_text = "list(1 2 3)"
        result = parse_lists(input_text)
        self.assertEqual(result, [["1", "2", "3"]])

    def test_parse_constants(self):
        input_text = "(define x 10);"
        result = parse_constants(input_text)
        self.assertEqual(result, {"x": 10})
