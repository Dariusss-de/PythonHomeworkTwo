# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.


number_N = int(input('Введите количество элементов списка: '))
nums = []
value = 1
for i in range(1, number_N + 1):
    nums.append(value)
    value *= i + 1
print(nums)