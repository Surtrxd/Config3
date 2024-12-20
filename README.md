# Config3: Инструмент командной строки для работы с конфигурационным языком

## Описание
Config3 — это инструмент командной строки для анализа и преобразования текста на учебном конфигурационном языке в формат YAML. Программа поддерживает разбор констант, списков, вычисляемых выражений и комментариев, а также обработку синтаксических ошибок.

## Возможности
- Поддержка синтаксиса конфигурационного языка:
  - Многострочные комментарии (`#| ... |#`).
  - Объявление констант `(define имя значение);`.
  - Списки `list(значение1 значение2 ...)`.
  - Выражения с арифметикой и вызовом функций `?[имя + 1]`.
- Выявление и обработка синтаксических ошибок.
- Вывод результата в формате YAML.

## Требования
- Python 3.6 или выше.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Surtrxd/Config3.git
   cd Config3

Использование

Запустите инструмент с указанием пути к входному файлу:

`python cli.py --input path/to/config_file.txt`


# Пример 1: Математические расчеты
(define x 10);
(define y 20);
?[x + y];
?[x - y];

# Пример 2: Работа с вложенными массивами
(define nested_list (list (list 1 2) (list 3 4) 5));
(define sorted_nested ?[sort(nested_list)]);


# Итог:

``` 
Текст после загрузки:
 #| Проверяем многострочные
комментарии. Этот текст
должен быть удалён. |#

(define x 10);
(define y 20);
(define z 5);

list(1 2 3)
list('a' 'b' 'c')
list(list(1 2) list(3 4) 5)

(define example_list (list 5 2 3 1 4));
(define sorted_list ?[sort(example_list)]);

?[x + y]
?[y - z]
?[x * z]


Текст после удаления комментариев:


(define x 10);
(define y 20);
(define z 5);

list(1 2 3)
list('a' 'b' 'c')
list(list(1 2) list(3 4) 5)

(define example_list (list 5 2 3 1 4));
(define sorted_list ?[sort(example_list)]);

?[x + y]
?[y - z]
?[x * z]


Найденные константы: {'x': 10, 'y': 20, 'z': 5, 'example_list': [5, 2, 3, 1, 4]}

Результаты вычислений: [[1, 2, 3, 4, 5], 30, 15, 50]

Итоговый YAML:
constants:
  x: 10
  y: 20
  z: 5
  example_list:
  - 5
  - 2
  - 3
  - 1
  - 4
lists:
- - a
  - b
  - c
- - 1
  - 2
  - 3
- - list1 2
- - 3
  - 4
expressions:
- - 1
  - 2
  - 3
  - 4
  - 5
- 30
- 15
- 50
 ```

# Возможные ошибки и их решения:

1. Ошибка: "Файл не найден"

- Проверьте правильность пути к файлу, переданного через --input.

2. Ошибка синтаксиса

- Убедитесь, что входной файл соответствует поддерживаемому синтаксису.

3. Выражение не вычислено

- Проверьте, что все константы, используемые в выражениях, определены ранее.


