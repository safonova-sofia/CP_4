import random
maximum = -10**10
index = 0

while True:
    array_len = input("Введите размерность массива: ")
    if array_len.isdigit() and array_len[0] != '0':
        break
    else:
        print("Ошибка при вводе данных. Повторите ввод.")

array = [0] * int(array_len)

for i in range(int(array_len)):
    array[i] = float(format(random.triangular(-5, 5), '.1f'))
print("Массив:", array)

for i in range(int(array_len)):
    if array[i] > maximum:
        index = i
        maximum = array[i]
print("Максимальный элемент", maximum, "\nИндекс максимального элемента:", index)

for i in range(index + 1,int(array_len)):
    array[i] = 0
print("Преобразованный массив:", array)




