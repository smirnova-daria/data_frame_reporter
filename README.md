# DataFrame Reporter

Это единый инструмент для первичной диагностики данных.

Класс DataFrameReporter принимает любой датафрейм и выдает стандартный отчёт — количество строк и столбцов, дубликаты, сводную статистику и информацию о пропусках.

## Установка окружения и библиотек

1. Создание виртуального окружения:
```bash
python3 -m venv venv
```
2. Активация виртуального окружения:
```bash
# Windows
source venv/Scripts/activate

# Linux, Mac
source venv/bin/activate
```
3. Установка библиотек:
```bash
pip install -r requirements.txt
```
4. Запуск `main.py`:
```bash
python3 main.py
```