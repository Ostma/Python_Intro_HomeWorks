# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

def inputCoord(xy):
     numCheck = False
     while not numCheck:
        try:
            coord = int(input(f'Введите координату {xy} : '))
            numCheck = True
        except ValueError:
            print('Это не число, попробуйте снова')
     return coord

def quarter(x,y):
    quar = 4
    if x > 0 and y > 0:
        quar = 1
    elif x < 0 and y > 0:
        quar = 2
    elif x < 0 and y < 0:
        quar = 3
    return quar

coordX = inputCoord('x')
coordY = inputCoord('y')
if (coordX == 0) and (coordY == 0):
    print('Ошибка! Точка является точкой пересечения осей')
elif (coordX == 0) and (coordY != 0):
    print('Точка с указанными координатами лежит на оси X')
elif (coordX != 0) and (coordY == 0):
    print('Точка с указанными координатами лежит на оси Y')
else:
    print(f'Точка с координатами x={coordX} и y={coordY} принадлежит {quarter(coordX, coordY)} четверти')