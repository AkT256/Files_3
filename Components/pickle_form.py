import pickle


def load_table(filepath):
    """Загружает таблицу из pickle-файла.
    Args:
        filepath: Путь к pickle-файлу.
    Returns:
        Список списков (таблица) из файла, или None при ошибке.
    Raises:
        FileNotFoundError: Если файл не найден.
        Exception: При других ошибках.
    """
    try:
        with open(filepath, 'rb') as picklefile:
            data = pickle.load(picklefile)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    except Exception as e:
        raise Exception(f"Ошибка загрузки pickle-файла: {e}")
    return data

def save_table(filepath, table):
    """Сохраняет таблицу в pickle-файл.
    Args:
        filepath: Путь к pickle-файлу.
        table: Список списков(таблица) для сохранения.
    Raises:
        Exception: При ошибках сохранения.
    """
    try:
        with open(filepath, 'wb') as picklefile:
            pickle.dump(table, picklefile)
    except Exception as e:
        raise Exception(f"Ошибка сохранения pickle-файла: {e}")