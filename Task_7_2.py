# Написать программу, со следующим интерфейсом: пользователю предоставляется на
# выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
# от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат. Использовать функции из первого
# задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.

from Task_7_1 import inch_to_sm, sm_to_inch, mi_to_km, km_to_mi, fu_to_kg, kg_to_fu, unz_to_g, g_to_unz, gal_to_l, \
    l_to_gal, pint_to_l, l_to_pint





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

