## python-скрипты

**ipsfromfile.py** - извлечение ip-адресов из файла с текстовым мусором, использование `ipsfromfile <filename>`.

**telsfromfile.py** - извлечение мобильных номеров телефонов из файла с текстовым мусором, использование `telsfromfile <filename>`.

> Внимание! Для более удобного способа работы со скриптами, выполняем следующие действия:
```bash
# 1. Создаем директорию для хранения скриптов:
mkdir ~/scripts

# 2. Копируем скрипты:
~/scripts/ipsfromfile.py
~/scripts/telsfromfile.py

# 3. Назначаем права на запуск
chmod +x ~/scripts/ipsfromfile.py
chmod +x ~/scripts/telsfromfile.py

# 4. Добавлеям псевдонимы в файл ~/.bashrc
nano ~/.bashrc
# alias ipsfromfile=~/scripts/ipsfromfile.py
# alias telsfromfile=~/scripts/telsfromfile.py

# 5. Перегружаем .bashrc в окружение
source ~/.bashrc

# ... теперь из места любой локации, скрипты будут работать
ipsfromfile ips-recycled.txt
telsfromfile tels-recycled.txt
```