# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите число: '))
max_number = 0

while max_number < user_number % 10:
    max_number = user_number % 10
    user_number //= 10

print(max_number)




