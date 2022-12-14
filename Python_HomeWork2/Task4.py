#  По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
#  При этом каждый из тех, кто участвовал в этом счете, получил по одной монете,
#  остальные получили по две монеты. Далее человек, на котором остановился счет,
#  отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
#  Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
#  Составьте алгоритм, который проводит эту игру.
#  Определите номер этого человека и количество монет, которые оказались у него в конце игры.

def input_num(message, max_num):
    numCheck = False
    while not numCheck:
        try:
            num = int(input(f'Введите {message} : '))
            numCheck = True
            if num < 1 or num > max_num:
                numCheck = False
                print(f'Комп старенький, такие расчеты не потянет, введите от 1 до {max_num}')
        except ValueError:
            print('Это не число, попробуйте снова')
    return num



lyudey = input_num('сколько будет людей в круге (1-100)', int(100))
ostatok_lyudey = lyudey
coin = [0 for x in range(lyudey)]
lyudi = list(range(1, lyudey + 1))

while len(lyudi) > 1:
    coin = [i+1 for i in coin]
    index_zhertva = (int(input (f'Введите номер участника от 1 до {len(lyudi)}: '))) - 1
    temp = index_zhertva
    while index_zhertva < len(lyudi):
        # print(index_zhertva, coin[index_zhertva])
        coin[index_zhertva] = coin[index_zhertva] +1
        index_zhertva = index_zhertva + 1


    print(f'\перед удалением\n{coin} , {lyudi}')
    ostatok_zhertvy = coin.pop(temp)
    del lyudi[temp]
    if temp + 1 > len(lyudi):
        coin[1] = coin[temp+1] + ostatok_zhertvy
    else:
        coin[temp + 1] = coin[temp+1] + ostatok_zhertvy
        print(f'\после удаления\n{coin} , {lyudi}')

