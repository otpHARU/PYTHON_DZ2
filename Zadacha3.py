# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.


number = int(input('Введите число: '))
list = []
i = 0
summ = 0
print(f'Список чисел: ', end='')

while i < number:
     list.append((1 + (1 / (i + 1))) ** (i + 1))
     list[i] = round(list[i])
     summ = summ + list[i]
     i = i + 1
print(list)
print(f'Сумма списка чисел:', summ)















