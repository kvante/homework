# Создать функцию, которая принимает на вход
# неопределенное количество именных
# аргументов и выводит на экран те из них,
# длина ключа которых четна

def new_list(**kwargs):
    for i in kwargs:
        if len(i) % 2 == 0:
            print(i)


new_list(a=2, b=3, ff=4)
