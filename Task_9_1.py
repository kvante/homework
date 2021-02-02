# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.


list_string = ['hi', 'hello', 'goodbye']

list_format = [f'{list_string.index(i)+1} - {i}' for i in list_string]

print(list_format)

