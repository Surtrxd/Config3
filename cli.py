import argparse
import yaml  # Библиотека для формирования YAML
from config_parser.parser import preprocess_text, remove_comments  # Исправленный импорт

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--input", help="Путь к файлу с конфигурацией")
    args = arg_parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            input_text = f.read()

        # Выполняем предварительную обработку
        constants, lists_parsed, expressions = preprocess_text(input_text)

        # Формируем итоговый результат
        result = {
            "constants": constants,
            "lists": [list(x) for x in set(tuple(l) for l in lists_parsed)],  # Убираем дубликаты списков
            "expressions": expressions
        }

        # Вывод результатов
        print("Текст после загрузки:\n", input_text)
        print("\nТекст после удаления комментариев:\n", remove_comments(input_text))
        print("\nНайденные константы:", constants)
        print("\nРезультаты вычислений:", expressions)
        print("\nИтоговый YAML:")
        print(yaml.dump(result, allow_unicode=True, sort_keys=False))
