# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число,
# и что это действительно входит в нужный диапазон

day = input('Введите день недели: ')
if day.isdigit() == True: #Проверили, что введенная переменная состоит из цифр
    if 6 < int(day) < 8:
        print('Этот день - выходной') #Если 6 или 7 - пишем что выходной
    elif 1 <= int(day) < 6:
        print('Этот день рабочий') #Если от 1 до 5 - пишем, что рабочий
    else:
        print('Нет такого дня недели') #Если число не подпадает ни под первое сравнение, ни под второе
else:
    print('Вы ввели не число') #Сообщение, если ввели не число