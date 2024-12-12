def save_table(filepath, table):
    """Сохраняет таблицу в текстовый файл.
    Args:
        filepath: Путь к текстовому файлу.
        table: Список списков (таблица) для сохранения.
    Raises:
        Exception: При ошибках сохранения.
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as textfile:
            for row in table:
                textfile.write('\t'.join(str(row)) + '\n')
    except Exception as e:
        raise Exception(f"Ошибка сохранения текстового файла: {e}")
