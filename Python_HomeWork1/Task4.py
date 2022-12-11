# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).


numCheck = False
while not numCheck:
    try:
        quar = int(input('Введите номер четверти (1-4): '))
        numCheck = True
        if (quar < 1) or (quar > 4):
            numCheck = False
            print('Число должно быть от 1 до 4 вкл.!')
    except ValueError:
        print('Это не число, попробуйте снова')

if quar == 1:
    print ('Первая четверть - x∈(0, ∞) u y∈(0,∞)')
elif quar == 2:
    print ('Вторая четверть - x∈(-∞, 0) u y∈(0,∞)')
elif quar == 3:
    print ('Третья четверть - x∈(-∞, 0) u y∈(-∞,0)')
else: print ('Четвертая четверть - x∈(0, ∞) u y∈(-∞,0)')