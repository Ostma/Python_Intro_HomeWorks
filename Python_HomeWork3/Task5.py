def fibo_pol(n, pos):
    a1 = a0 = 1
    for n in range(int(n)):
        pos.append(a1)
        temp = a0 + a1
        a1 = a0
        a0 = temp
    return pos

def fibo_neg(n, pos):
    b1 = 0
    b2 = 1
    for n in range(int(n+1)):
        pos.insert(0, b1)
        temp = b1 - b2
        b1 = b2
        b2 = temp
    return pos



posled = []
num_check = False
while not num_check:
    try:
        len = int(input('Какой длины будет последовательность: '))
        num_check = True
        if len < 2 or len > 100:
            num_check = False
            print('Хватит шутить, введи от 2 до 100')
    except ValueError:
        print('Это не число, попробуйте снова')

fibo_pol(len, posled)
fibo_neg(len, posled)
print (f'Ряд Фибоначчи будет\n {posled}')
    
 
