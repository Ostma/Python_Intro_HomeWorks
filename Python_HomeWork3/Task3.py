# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

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


arr = [(random.randrange(0, 50000))/1000 for i in range(arr_len)]
print(f'Пусть массив будет {arr}')

new_arr = []

# new_arr = [(arr[j] - math.trunc((arr[j]))) for j in range(arr_len)]
new_arr = [round((arr[j] % math.trunc((arr[j]))), 5) for j in range(arr_len)]
print(new_arr)

print (f'Разница между максимальным и минимальным равна {max(new_arr) - min(new_arr)}')