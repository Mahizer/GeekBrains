# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


time_in_seconds = int(input('Введите время в секундах: '))

hour = time_in_seconds // 3600
minute = (time_in_seconds % 3600) // 60
second = time_in_seconds % 6

print(f'{hour:02.0f}:{minute:02.0f}:{second:02.0f}')
