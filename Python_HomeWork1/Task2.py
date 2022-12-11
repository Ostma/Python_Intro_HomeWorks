# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.
print('\n\n           ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
print("_________________________________________________\n x  |  y  |  z  |  left  |  right       |  result\n_________________________________________________")
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            left = not(x or y or z)
            right = (not x) and (not y) and (not z)
            print(f"{x}  | {y}  | {z}  | {left}  | {right}  | {left==right}")