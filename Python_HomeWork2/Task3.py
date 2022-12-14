# Дан массив размера N. После каждого отрицательного элемента массива
# вставьте элемент с нулевым значением.

import random
import array as arr
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


arr = [random.randint(-1000, 1000) for i in range(arr_len)]
print(f'Пусть массив будет {arr}')

j = 0
while j <= arr_len:
    if arr[j] < 0:
        arr.insert(j + 1, 0)
    j += 1
print(arr)