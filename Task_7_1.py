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
    return n * 4.55  # , n * 3.79  # england ad american


def l_to_gal(n):
    return n / 4.55  # , n / 3.79  # england ad american


def pint_to_l(n):
    return n * 0.57  # , n * 0.47  # england ad american


def l_to_pint(n):
    return n / 0.57  # , n / 0.47  # england ad american


print(' \n',
      '1. Дюймы в сантиметры\n',
      '2. Сантиметры в дюймы\n',
      '3. Мили в километры\n',
      '4. Километры в мили\n',
      '5. Фунты в килограммы\n',
      '6. Килограммы в фунты\n',
      '7. Унции в граммы\n',
      '8. Граммы в унции\n',
      '9. Галлон в литры\n',
      '10. Литры в галлоны\n',
      '11. Пинты в литры\n',
      '12. Литры в пинты\n',
      '0. Выход\n')

while True:
    a = input('Введите номер операции: ')

    if a.isdigit() and 0 <= int(a) <= 12:
        a = int(a)

        if a == 0:
            break

        b = input('Ввести численное значение: ').replace(',', '.')

        if b.isdigit() and type(b) == int or float:

            b = float(b)

            if a == 1:
                print(inch_to_sm(b))
            if a == 2:
                print(sm_to_inch(b))
            if a == 3:
                print(mi_to_km(b))
            if a == 4:
                print(km_to_mi(b))
            if a == 5:
                print(fu_to_kg(b))
            if a == 6:
                print(kg_to_fu(b))
            if a == 7:
                print(unz_to_g(b))
            if a == 8:
                print(g_to_unz(b))
            if a == 9:
                print(gal_to_l(b))
            if a == 10:
                print(l_to_gal(b))
            if a == 11:
                print(pint_to_l(b))
            if a == 12:
                print(l_to_pint(b))
        else:
            print('не верно')
    else:
        print('не верно')
