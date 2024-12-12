def get_rows_by_number(data, start, stop=None, copy_table=False):
    """
    Возвращает строки таблицы по их номерам.
    Args:
        data: Данные таблицы (список списков).
        start: Начальный индекс строки (включительно).
        stop: Конечный индекс строки (не включительно). Если None, возвращается одна строка.
        copy_table: Если True, возвращается копия данных.
    Returns:
        Список строк (список списков).
    Raises:
        ValueError: Если start или stop вне допустимого диапазона или start >= stop.
        TypeError: Если входные данные имеют некорректный тип.
    """
    try:
        if stop is None:
            stop = start + 1
        if start < 0 or stop > len(data) or start >= stop:
            raise ValueError("Неверные индексы строк.")
        if copy_table:
            return [row[:] for row in data[start:stop]]  # Создаем копии строк
        return data[start:stop]
    except Exception as e:
        raise type(e)(f"Ошибка в get_rows_by_number: {e}")


def get_rows_by_index(data, *vals, copy_table=False):
    """
    Возвращает строки, где значение первого столбца совпадает с одним из vals.
    Args:
        data: Данные таблицы (список списков).
        vals: Значения для поиска в первом столбце.
        copy_table: Если True, возвращается копия данных.
    Returns:
        Список строк (список списков).
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если таблица пуста или строки имеют разную длину.
    """
    try:
        result = [row for row in data if row[0] in vals]
        if copy_table:
            return [row[:] for row in result]  # Создаем копии строк
        return result
    except Exception as e:
        raise type(e)(f"Ошибка в get_rows_by_index: {e}")


def get_column_types(data, by_number=True):
    """
    Определяет типы данных в каждом столбце.
    Args:
        data: Данные таблицы (список списков).
        by_number: Если True, ключи - номера столбцов; иначе - заголовки.
    Returns:
        Словарь {номер_столбца/заголовок: тип_данных}.
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если таблица пуста или имеет некорректную структуру.
    """
    try:
        types = {}
        if not data:
            raise IndexError("Таблица пуста.")
        num_cols = len(data[0])
        for i in range(num_cols):
            col_data = [row[i] for row in data]
            col_type = type(next((item for item in col_data if item is not None),None)) if col_data else type(None)
            types[i if by_number else data[0][i]] = col_type
        return types
    except Exception as e:
        raise type(e)(f"Ошибка в get_column_types: {e}")


def set_column_types(data, types_dict, by_number=True):
    """
    Приводит типы данных в столбцах к указанным.
    Args:
        data: Данные таблицы (список списков).
        types_dict: Словарь {номер_столбца/заголовок: тип_данных}.
        by_number: Если True, ключи - номера столбцов; иначе - заголовки.
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если столбец не найден.
        ValueError: Если преобразование типов невозможно.
    """
    try:
        for key, col_type in types_dict.items():
            if by_number:
                col_index = key
            else:
                col_index = data[0].index(key)
            for row in data:
                if row[col_index] is not None:
                    row[col_index] = col_type(row[col_index])
    except Exception as e:
        raise type(e)(f"Ошибка в set_column_types: {e}")


def get_values(data, column=0):
    """
    Возвращает значения из указанного столбца.
    Args:
        data: Данные таблицы (список списков).
        column: Индекс столбца.
    Returns:
        Список значений.
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если индекс столбца вне диапазона.
    """
    try:
        return [row[column] for row in data]
    except Exception as e:
        raise type(e)(f"Ошибка в get_values: {e}")


def get_value(data, column=0):
    """
    Возвращает значение из указанного столбца первой строки.
    Args:
        data: Данные таблицы (список списков).
        column: Индекс столбца.
    Returns:
        Значение.
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если индекс столбца вне диапазона.
    """
    try:
        return data[0][column]
    except Exception as e:
        raise type(e)(f"Ошибка в get_value: {e}")

def set_values(data, values, column=0):
    """
    Записывает значения в указанный столбец.
            Args:
                data: Данные таблицы (список списков).
                values: Список значений для записи.
                column: Индекс столбца.
            Raises:
                TypeError: Если входные данные имеют некорректный тип.
                IndexError: Если индекс столбца или длина values не соответствуют размеру таблицы.
            """
    if len(values) > len(data):
        raise IndexError("Длина списка значений превышает количество строк в таблице.")
    try:
        for i, value in enumerate(values):
            data[i][column] = value
    except (IndexError, TypeError) as e:
        raise type(e)(f"Ошибка в set_values: {e}")

def set_value(data, value, column=0):
    """
    Записывает значение в указанную ячейку.
    Args:
        data: Данные таблицы (список списков).
        value: Значение для записи.
        column: Индекс столбца.
    Raises:
        TypeError: Если входные данные имеют некорректный тип.
        IndexError: Если индекс столбца вне диапазона.
    """
    try:
        if len(data) != 1:
            raise ValueError("Функция set_value() работает только с таблицами с одной строкой.")
        index = column
        data[0][index] = value
    except Exception as e:
        raise type(e)(f"Ошибка в set_value: {e}")

def print_table(data):
    """Выводит таблицу на консоль."""
    try:
        for row in data:
            print('\t'.join(map(str, row)))
    except Exception as e:
        raise type(e)(f"Ошибка в print_table: {e}")