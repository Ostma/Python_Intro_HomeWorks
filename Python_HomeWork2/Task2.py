# Напишите программу, которая принимает на вход число N
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.


numCheck = False
while not numCheck:
    try:
        num = int(input('Введите число : '))
        numCheck = True
        if num < 1 or num > 20:
            numCheck = False
            print('Комп старенький, такие расчеты не потянет, введите от 1 до 20')
    except ValueError:
        print('Это не число, попробуйте снова')
fac = []
i = 1
while i <= num:
    i += 1
    j = 1
    temp = 1
    while j < i:
        temp = temp * j
        j += 1
    fac.append(temp)
print (fac)