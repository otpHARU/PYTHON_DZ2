# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


number = int(input('Введите число: '))
factorial = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( factorial(i) for i in range(1, number +1))
print(f"Произведения чисел от 1 до {number}:  {list2}")

