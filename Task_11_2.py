# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
# умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
# разворот(изменение знака скорости). Все атрибуты приватные.

class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_increase(self):
        self.__speed += 5
        return self.__speed

    def speed_reduction(self):
        self.__speed -= 5

    def speed_stop(self):
        self.__speed = 0

    def speed_view(self):
        return self.__speed

    def speed_reverse(self):
        self.__speed = -self.__speed


car1 = Car('toyota', 'mark1', 1999)

car1.speed_increase()
car1.speed_increase()
car1.speed_reduction()
car1.speed_increase()

print(car1.speed_view())
