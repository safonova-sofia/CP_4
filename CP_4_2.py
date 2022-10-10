import random

maximum = -10 ** 10
index = 0

while True:
    array_len_A = input("Введите размерность массива A: ")
    if array_len_A.isdigit() and array_len_A[0] != '0':
        break
    else:
        print("Ошибка при вводе данных. Повторите ввод.")

while True:
    array_len_B = input("Введите размерность массива B: ")
    if array_len_B.isdigit() and array_len_B[0] != '0':
        break
    else:
        print("Ошибка при вводе данных. Повторите ввод.")

while True:
    a = input("Введите нижнюю целую границу допустимых значение в массиве: ")
    if len(a) == 1 and a.isdigit():
        break
    elif len(a) > 1:
        if a[0] == '-' and a[1:].isdigit() or a.isdigit():
            break
    print("Ошибка при вводе данных. Повторите ввод.")

while True:
    b = input("Введите верхнюю целую границу допустимых значение в массиве: ")
    if len(b) == 1 and b.isdigit():
        break
    elif len(b) > 1:
        if b[0] == '-' and b[1:].isdigit() or b.isdigit():
            break
    print("Ошибка при вводе данных. Повторите ввод.")

a = int(a)
b = int(b)
array_len_A = int(array_len_A)
array_len_B = int(array_len_B)

array_A = [0] * array_len_A
array_B = [0] * array_len_B

for i in range(array_len_A):
    array_A[i] = random.randint(a, b)
print("Массив A:", array_A)

for i in range(array_len_B):
    array_B[i] = random.randint(a, b)
print("Массив B:", array_B)

array_both = [0] * (b - a + 1)

for i in range(array_len_A):
    for j in range(array_len_B):
        if ((array_A[i] == array_B[j]) and (array_both[array_A[i] - a] == False)):
            array_both[array_A[i] - a] = True
            break

for i in range(len(array_both)):
    if array_both[i] == True:
        print("Элемент общий для A и B:", i + a)


