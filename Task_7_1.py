# Написать 12 функций по переводу:
#
# Дюймы в сантиметры
# Сантиметры в дюймы
# Мили в километры
# Километры в мили
# Фунты в килограммы
# Килограммы в фунты
# Унции в граммы
# Граммы в унции
# Галлон в литры
# Литры в галлоны
# Пинты в литры
# Литры в пинты
# Примечание: функция принимает на вход число и возвращает конвертированное число

def inch_to_sm(n):
    return n * 2.54


def sm_to_inch(n):
    return n / 2.54


def mi_to_km(n):
    return n * 1.61


def km_to_mi(n):
    return n / 1.61


def fu_to_kg(n):
    return n * 0.45


def kg_to_fu(n):
    return n / 0.45


def unz_to_g(n):
    return n * 28.35


def g_to_unz(n):
    return n / 28.35


def gal_to_l(n):
    return n * 4.55, n * 3.79  # england ad american


def l_to_gal(n):
    return n / 4.55, n / 3.79  # england ad american


def pint_to_l(n):
    return n * 0.57, n * 0.47  # england ad american


def l_to_pint(n):
    return n / 0.57, n / 0.47  # england ad american
