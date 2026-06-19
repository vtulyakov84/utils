#!/usr/bin/env python3

import re
import sys
import os

def find_ips(filename):
    """
    Поиск IP-адресов с более точным регулярным выражением
    """
    # Более точное регулярное выражение для IPv4
    ip_pattern = r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    
    try:
        with open(filename, 'r', encoding='cp1251') as file:
        #with open(filename, 'r') as file:
            content = file.read()

        # Находим все IP-адреса
        matches = re.finditer(ip_pattern, content)
        ips = [match.group() for match in matches]

        return ips
        
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
        print("Идея: Извлечение ip-адресов из текстового файла")
        print("Кодировка входного файла: cp1251")
        print("Пример использования: `./ipfromfile.py file-name`")
        sys.exit(1)

    file_name = sys.argv[1]

    # Проверяем существование файла
    if not os.path.isfile(file_name):
        print(f"Останов. Не найден файл `{file_name}`. Или указана директория.")
        sys.exit(1)
    

    # Использование
    ips = find_ips(file_name)
    print(f"Найдено IP-адресов: {len(ips)}")
    for ip in ips:
        print(ip)
