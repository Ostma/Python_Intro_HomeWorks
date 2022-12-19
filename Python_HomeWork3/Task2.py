# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
import math
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

arr = [random.randint(1, 21) for i in range(arr_len)]
print(f'Пусть массив будет {arr}')

out_arr = []
temp = 0
for i in range(0, math.ceil(arr_len / 2)):
    out_arr.append((arr[i] * arr[(-i)-1]))

print (out_arr)