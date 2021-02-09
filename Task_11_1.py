# Создать пять классов описывающие реальные объекты. Каждый класс
# должен содержать минимум три приватных атрибута, конструктор, геттеры
# и сеттеры для каждого атрибута, два метода.


class Dog:
    def __init__(self, name, age, speed):
        self.__name = name
        self.__age = age
        self.__speed = speed
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed

class Cat:
    def __init__(self, name, age, speed):
        self.__name = name
        self.__age = age
        self.__speed = speed
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
class Bird:
    def __init__(self, name, age, speed):
        self.__name = name
        self.__age = age
        self.__speed = speed
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
class Fish:
    def __init__(self, name, age, speed):
        self.__name = name
        self.__age = age
        self.__speed = speed
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed
class Home:
    def __init__(self, city, street, building):
        self.__city = city
        self.__street = street
        self.__building = building
    def get_city(self):
        return self.__city
    def set_name(self, city):
        self.__city = city
    def get_street(self):
        return self.__street
    def set_age(self,street):
        self.__street = street
    def get_speed(self):
        return self.__building
    def set_speed(self, building):
        self.__building = building