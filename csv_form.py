import csv


def load_table(filepath):
    """Загружает таблицу из CSV-файла.
    Args:
        filepath: Путь к CSV-файлу.
    Returns:
        Список списков (таблица) из файла, или None при ошибке.
    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: При других ошибках.
    """
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    except Exception as e:
        raise Exception(f"Ошибка загрузки CSV-файла: {e}")


def save_table(filepath, table):
    """Сохраняет таблицу в CSV-файл.
    Args:
        filepath: Путь к CSV-файлу.
        table: Список списков (таблица) для сохранения.
    Raises:
        Exception: При ошибках сохранения.
    """
    try:
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)
    except Exception as e:
        raise Exception(f"Ошибка сохранения CSV-файла: {e}")