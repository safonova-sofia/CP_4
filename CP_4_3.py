import random

minimum = 10 ** 10
count = 0

while True:
    array_len = input("Введите размерность массива: ")
    if array_len.isdigit() and array_len[0] != '0':
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

while True:
    delta = input("Введите дельту: ")
    if len(delta) == 1:
        if delta.isdigit():
            break
    elif len(delta) > 1:
        if delta[0] == '-' and delta[1:].isdigit() or delta.isdigit():
            break
    print("Ошибка при вводе данных. Повторите ввод.")

a = int(a)
b = int(b)
array_len = int(array_len)
delta = int(delta)

print("Длина массива:", array_len)

array = [0] * array_len

for i in range(array_len):
    array[i] = random.randint(a, b)
print("Массив:", array)

for i in array:
    if i < minimum:
        minimum = i
print("Минимальный элемент:", minimum)

for i in array:
    if minimum + delta == i:
        count += 1
print("Кол-во элементов, отличающихся от минимального на дельта:", count)