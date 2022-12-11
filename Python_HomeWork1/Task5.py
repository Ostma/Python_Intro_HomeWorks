# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Формула вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости:
# AB = √(xb - xa)2 + (yb - ya)2

def inputCoord(xy):
     numCheck = False
     while not numCheck:
        try:
            coord = int(input(f'Введите координату {xy} : '))
            numCheck = True
        except ValueError:
            print('Это не число, попробуйте снова')
     return coord

ax = inputCoord ('X точки А')
ay = inputCoord ('Y точки А')
bx = inputCoord ('X точки B')
by = inputCoord ('Y точки B')
res = ((bx - ax)**2 + (by - ay)**2)**0.5
print(f'Расстояние между точками А и В равно {round(res, 5)}')