# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.


def my_decorator(func):
    def my_func():
        a = func()
        a = [i for i in reversed(a)]
        print(a)
    return my_func()

@my_decorator
def list_a():
    a = [i for i in range(11)]
    return a