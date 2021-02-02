# Создать lambda функцию, которая принимает на вход неопределенное
# количество именных аргументов и выводит словарь с ключами удвоенной
# длины. {‘abc’: 5} -> {‘abcabc’: 5}


my_function = lambda **kwargs: {k*2: v for k, v in kwargs.items()}

print(my_function(a=2, b=3))