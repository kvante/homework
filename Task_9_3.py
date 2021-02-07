# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.



def my_decorator(func):

    def my_func():
        a = func()
        a = [x for x in a if x % 2]
        print(a)

    return my_func()


@my_decorator
def my():
    a = [i for i in range(20)]
    return a
