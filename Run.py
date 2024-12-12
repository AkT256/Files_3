from xmlrpc.client import boolean

from Components import csv_form,pickle_form,txt_form,SecondaryOperations

#Задание таблиц
# Тестовые таблицы
first_table = [
    ["Name", "Age", "City"],

        ["Ivan", "20", "Moscow"],
        ["Denis", "25", "London"],
        ["Anna", "30", "Random_City"],
        ["Paul", "23", "Paris"]

]

table1 = [
    ["Name", "Age", "City"],
]

table2 = [
    ["Name", "Age", "City"],
    ["Anna", "30", "Random_City"], ["Paul", "23", "Paris"]
]

# Сохранение таблицы
csv_form.save_table('file1.csv',first_table)

# Загрузка таблицы
data = csv_form.load_table('file1.csv')


# Примеры использования функций
print("Значения из столбца 'Age':", SecondaryOperations.get_values(data, column=1))
print("Значение из столбца 'City' первой строки:", SecondaryOperations.get_value(data, column=2))


pickle_form.save_table('file2.pkl',table1)
data1 = pickle_form.load_table('file2.pkl')

# Установка значения в столбец 'City' первой строки
SecondaryOperations.set_value(data1, 'New_York', column=2)#------------------------------

# Вывод обновленной таблицы на экран
SecondaryOperations.print_table(data)


# Сохранение таблицы pickle_form
pickle_form.save_table('file2.pkl',table1)

# Загрузка таблицы pickle_form
data1 = pickle_form.load_table('file2.pkl')

SecondaryOperations.print_table(data1)

# Сохранение таблицы txt_form
txt_form.save_table('file3.txt',table2)

print("Возвращает строки таблицы по их номерам")
strings = SecondaryOperations.get_rows_by_number(first_table, 0, 3, copy_table=True)
SecondaryOperations.print_table(strings)

# Получение строк по значению в первом столбце
print("Получение строк по значению в первом столбце")
inf = SecondaryOperations.get_rows_by_index(first_table, "Ivan", copy_table=True)
SecondaryOperations.print_table(inf)

# Получение типов столбцов
print("Получение типов столбцов")
column_types = SecondaryOperations.get_column_types(first_table)
print(column_types)

# Установка типов столбцов
print("Установка типов столбцов")
SecondaryOperations.set_column_types(first_table, {1: bool, 2: str}, by_number=True)
SecondaryOperations.print_table(first_table)

# Получение значений столбца
print("Получение значений столбца")
ages =  SecondaryOperations.get_values(first_table, 1)
print(ages)

# Установка значений в столбец
print("Установка значений в столбец")
SecondaryOperations.set_values(first_table, [14,46, 74, 21], 1)
SecondaryOperations.print_table(first_table)