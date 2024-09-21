
##Задача 1. Сумма первых n положительных чисел
#n = int(input("Введите натуральное положительное число: "))
#sum_nat_num = (n * (n + 1)) // 2
##print(f"Сумма первых {n} натуральных чисел равна {sum_nat_num}.")
# print("Сумма положительных {} чисел равна {}.".format (n, sum_nat_num))


## Задача 2. Калькулятор
#import math

## Запрашиваем у пользователя два целых числа
#num1 = int(input("Введите первое целое число: "))
#num2 = int(input("Введите второе целое число: "))

# user_input = input("Введите два целых числа через запятую (например, 5,10): ")
#
# num1, num2 = map(int, user_input.split(','))
#
# print("\nАрифметические операции:")
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
#
# if num2 != 0:
#     print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
#     print(f"{num1} // {num2} = {num1 // num2}")
#     print(f"{num1} % {num2} = {num1 % num2}")
# else:
#     print(f"{num1} / {num2} = деление на ноль!")
#     print(f"{num1} // {num2} = деление на ноль!")
#     print(f"{num1} % {num2} = деление на ноль!")
#
# print(f"{num1} ** {num2} = {num1 ** num2}")
#
# if num1 > 0:
#     print(f"log10({num1}) = {round(math.log10(num1), 2)}")
# else:
#     print(f"log10({num1}) = логарифм не определен для num1 <= 0")
#
# print("\nОперации сравнения:")
# print(f"{num1} < {num2}  = {num1 < num2}")
# print(f"{num1} <= {num2} =2> {num1 <= num2}")
# print(f"{num1} > {num2}  = {num1 > num2}")
# print(f"{num1} >= {num2} = {num1 >= num2}")
# print(f"{num1} != {num2} = {num1 != num2}")
# print(f"{num1} == {num2} = {num1 == num2}")


# #Задача 3.
# # Запрашиваем у пользователя значения x, y и z
# x = int(input("Введите значение x: "))
# y = int(input("Введите значение y: "))
# z = int(input("Введите значение z: "))
#
# # Вычисляем значение выражения
# # (x ** 5 + 7) / (abs(-6) * y)
# numerator = (x ** 5 + 7)
# denominator = abs(-6) * y
# fraction = numerator / denominator
#
# # z % y (остаток от деления z на y)
# mod_result = z % y
#
# # Итоговое выражение
# f = fraction / (7 - mod_result)
#
# # Находим кубический корень
# result = f ** (1/3)
#
# # Округляем до 3 знаков после запятой
# rounded_result = round(result, 3)
#
# # Выводим результат
# print(f"Результат выражения: {rounded_result}")


# #Задача 4
# R1 = float(input("Введите сопротивление первого проводника (Ом): "))
# R2 = float(input("Введите сопротивление второго проводника (Ом): "))
#
# # Вычисляем общее сопротивление
# R_total = R1 + R2
#
# # Округляем результат до 1 знака после запятой
# R_total_rounded = round(R_total, 1)
#
# # Выводим результат
# print(f"Общее сопротивление цепи: {R_total_rounded} Ом")


# #Задача 5.
# a = int(input(f"Введите значение a: "))
# b = int(input(f"Введите значение b: "))
# m = int(input(f"Введите значение m : "))
# n = int(input(f"Введите значение n: "))
#
# if a == 0:
#     print("Коэффициент 'a' не должен быть равен нулю.")
# else:
#     # Решаем уравнение ax + b = 0
#     x = -b / a
#     print(f"Решение уравнения: x = {x}")
#
#     if (m <= n and m <= x <= n) or (m > n and (x >= n and x <= m)):
#         print(f"Решение уравнения x = {x} попадает в указанный отрезок [{m},{n}]")
#     else:
#         print(f"Решение уравнения x = {x} не попадает в указанный отрезок [{m},{n}]")

# #Задача 5.
# # Запрашиваем у пользователя скорость и время
# v = float(input("Введите скорость (в км/ч): "))
# t = float(input("Введите время (в часах): "))
#
# # Вычисляем общее расстояние
# distance = v * t
#
# # Определяем позицию на круге длиной 123 км
# position = distance % 123  # Остаток от деления показывает, где на круге
#
# # Выводим результат
# print(f"Спортсмен проедет {distance:.2f} км и остановится на километре: {int(position)}")


# # Функция для вычисления суммы и произведения цифр числа
# def sum_and_product_of_digits(number):
#     digits = [int(d) for d in str(number)]  # Извлекаем цифры числа
#     total_sum = sum(digits)  # Считаем сумму цифр
#     total_product = 1
#     for d in digits:
#         total_product *= d  # Считаем произведение цифр
#     return total_sum, total_product


# Запрашиваем двузначное число
two_digit_number = int(input("Введите двузначное число: "))
# Запрашиваем трехзначное число
three_digit_number = int(input("Введите трехзначное число: "))

# Вычисляем сумму и произведение цифр для двузначного числа
sum_two, product_two = sum_and_product_of_digits(two_digit_number)
print(f"Для двузначного числа {two_digit_number}: Сумма = {sum_two}, Произведение = {product_two}")

# Вычисляем сумму и произведение цифр для трехзначного числа
sum_three, product_three = sum_and_product_of_digits(three_digit_number)
print(f"Для трехзначного числа {three_digit_number}: Сумма = {sum_three}, Произведение = {product_three}")
