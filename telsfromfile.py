#!/usr/bin/env python3

import re
import sys
import os

def find_tels(filename):
    """
    Поиск Номером телефонов с более точным регулярным выражением
    """
    # Выборка 10-цифр, начинающихся с "9"
    tel_pattern = r'\b8\d{10}\b'
    
    try:
        with open(filename, 'r', encoding='cp1251') as file:
            content = file.read()

        # Находим все номера телефона
        matches = re.finditer(tel_pattern, content)
        tels = [match.group() for match in matches]

        return tels
        
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []



if __name__=='__main__':

    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        print("Автор: vtulyakov84@yandex.ru")
        print("Идея: Извлечение номеров телефонов из текстового файла")
        print("Кодировка входного файла: cp1251")
        print("Пример использования: `./telsfromfile.py file-name`")
        sys.exit(1)

    file_name = sys.argv[1]

    # Проверяем существование файла
    if not os.path.isfile(file_name):
        print(f"Останов. Не найден файл `{file_name}`. Или указана директория.")
        sys.exit(1)
    

    # Использование
    tels = find_tels(file_name)
    print(f"Найдено номеров тел.: {len(tels)}")
    for tel in tels:
        print(tel)
