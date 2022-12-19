# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
arr = []

num_check = False
while not num_check:
    try:
        arr_len = int(input('Какой длины будет массив? (2-100): '))
        num_check = True
        if arr_len < 2 or arr_len > 100:
            num_check = False
            print('Хватит шутить, введи от 2 до 100')
    except ValueError:
        print('Это не число, попробуйте снова')


arr = [random.randint(-20, 20) for i in range(arr_len)]
print(f'Пусть массив будет {arr}')

summ = 0
for i in range(1, arr_len):
    if i % 2 != 0:
        summ = summ + arr[i]

print(summ)