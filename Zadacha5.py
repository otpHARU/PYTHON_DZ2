# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

import random

number = int(input('Введите количество элементов (N): '))

j = number
n = range(0, number)
n = list(n)
print(f'Первоначальный список: ', n)
i = 0
while i < j:
    x = random.randint(0,j-1)
    n.remove(x)
    n.append(x)
    i = i + 1
print(f'Перемешанный список: ', n)



















