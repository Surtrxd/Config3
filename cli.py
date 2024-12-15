import argparse
from config_parser.parser import remove_comments, parse_lists, parse_constants, parse_expressions
from config_parser.transformer import transform_to_yaml

def main():
    parser = argparse.ArgumentParser(description="CLI для обработки конфигурационного языка.")
    parser.add_argument("--input", required=True, help="Путь к входному файлу")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            input_text = file.read()

        print(f"Текст после загрузки:\n{input_text}")
        clean_text = remove_comments(input_text)
        print(f"Текст после удаления комментариев:\n{clean_text}")
        lists = parse_lists(clean_text)
        print(f"Найденные списки: {lists}")
        constants = parse_constants(clean_text)
        print(f"Найденные константы: {constants}")
        expressions = parse_expressions(clean_text, constants)
        print(f"Результаты вычислений: {expressions}")

        data = {
            "lists": lists,
            "constants": constants,
            "expressions": expressions
        }

        yaml_output = transform_to_yaml(data)
        print("Итоговый YAML:")
        print(yaml_output)
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
