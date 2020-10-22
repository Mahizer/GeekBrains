# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите положительное число: '))

max_number = 0
while number != 0:
    last = number % 10
    if last >= max_number:
        max_number = last
    number = number // 10


print(max_number)



