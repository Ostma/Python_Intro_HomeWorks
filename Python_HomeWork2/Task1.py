# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# (-0.56) -> 11




# def manual_inp():
#     chk = False
# while not chk:
#     try:
#         number = float(input('Введи число: '))
#         chk = True
#     except ValueError:
#             print('Это не число, попробуйте снова')
#     return number



import random
variant = input('Сам число придумаешь, или случайное за тебя определить?\nВведите пробел если напишешь сам, любой другой символ, если хочешь случайное: ')

if variant == ' ':
    chk = False
    while not chk:
        try:
            num = float(input('Введи число: '))
            chk = True
        except ValueError:
                print('Это не число, попробуйте снова')
else:
    num = round(random.uniform (-100000, 100000),4)
    print(f'ОК, Пусть число будет {num}')

temp = str(num)
summ = int (0)

print(temp, summ)
for i in temp:
    if i.isdigit():
        summ = summ + int (i)


print(f'Сумма цифр числа {num} равна {summ}')

