# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

num_check = False
while not num_check:
    try:
        dec = int(input('Введи число: '))
        num_check = True
        if dec < 2:
            num_check = False
            print('Хватит шутить, введи от 2')
    except ValueError:
        print('Это не число, попробуйте снова')

bi = ""
while dec > 0:
    bi = str(dec % 2) + bi
    dec = dec // 2

print(f'Это число в двоичной системе будет {bi}')