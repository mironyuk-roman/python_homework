
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

# #Задача 6
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


# #Задача 7
# # Функция для вычисления суммы и произведения цифр числа
# def sum_and_product_of_digits(number):
#     digits = [int(d) for d in str(number)]  # Извлекаем цифры числа
#     total_sum = sum(digits)  # Считаем сумму цифр
#     total_product = 1
#     for d in digits:
#         total_product *= d  # Считаем произведение цифр
#     return total_sum, total_product
#
# # Запрашиваем двузначное число
# two_digit_number = int(input("Введите двузначное число: "))
# # Запрашиваем трехзначное число
# three_digit_number = int(input("Введите трехзначное число: "))
#
# # Вычисляем сумму и произведение цифр для двузначного числа
# sum_two, product_two = sum_and_product_of_digits(two_digit_number)
# print(f"Для двузначного числа {two_digit_number}: Сумма = {sum_two}, Произведение = {product_two}")
#
# # Вычисляем сумму и произведение цифр для трехзначного числа
# sum_three, product_three = sum_and_product_of_digits(three_digit_number)
# print(f"Для трехзначного числа {three_digit_number}: Сумма = {sum_three}, Произведение = {product_three}")


# #Задача 8
# # Запрашиваем у пользователя три целых числа
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
#
# # Находим минимальное и максимальное значение
# min_num = min(num1, num2, num3)
# max_num = max(num1, num2, num3)
#
# # Находим среднее число
# sum_of_numbers = num1 + num2 + num3
# middle_num = sum_of_numbers - min_num - max_num
#
# # Выводим числа в упорядоченном виде по возрастанию
# print(f"Числа в порядке возрастания: {min_num}, {middle_num}, {max_num}")


# #Задача 9. Поменять местами: не всё так просто!
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# a = a + b
# b = a - b
# a = a - b
# print(a, b)


# #Задача 10.
# team = input('Введите название футбольной команды: ')
# print(f'{team} - чемпион!')
# print('-' * len(team))
# team_lower = team.lower()
# print(f'Длина наименования команды: {len(team)}')
# print(f'Есть ли в наименовании команды буква "п"? {"п" in team_lower}')
# print(f'Сколько раз повторяется буква "а"? {team_lower.count("а")}')

# #Задача 11
# country = input("Введите название государства: ")
# capital = input("Введите столицу государства: ")
#
# print(f"Государство - {country}, столица - {capital}.")
#
# #Задача 12
# word = "объектно-ориентированный"
#
# word1 = word[0:6]    # "объект"
# word2 = word[8:16]   # "ориентир"
# word3 = word[12:15]  # "тир"
# word4 = word[3:6]    # "кот"
# word5 = word[9:14]   # "рента"
#
# print(word1)
# print(word2)
# print(word3)
# print(word4)
# print(word5)

# #Задача 13
# # Создать 2 пустых списка
# a = []
# b = []
#
# # Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
# a.append(4.5)
# a.append(3.4)
#
# # Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
# a.extend([8.7, 1.3])
#
# # Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
# b.append(14.5)
# b.append(3.4)
#
# # Добавить 2 вещественных числа (8.7, 11.3) в список 'b' с помощью extend
# b.extend([8.7, 11.3])
#
# # Вставить целое число 100 на 2-е и 4-е место списка 'a'
# a.insert(1, 100)
# a.insert(3, 100)
#
# # Вставить целое число 200 на 1-е и 3-е место списка 'b'
# b.insert(0, 200)
# b.insert(2, 200)
#
# # Вывести списки на экран
# print("Исходные списки:")
# print("1-й:", a)
# print("2-й:", b)
#
# # Удалить первые элементы из списков 'a' и 'b'
# del a[0]
# del b[0]
#
# # Удалить элемент 100 из списка 'a'
# a.remove(100)
# # Удалить элемент 200 из списка 'b'
# b.remove(200)
#
# # Вывести списки на экран
# print("\nПосле удалений:")
# print("1-й:", a)
# print("2-й:", b)
#
# # Создать множества из списков 'a' и 'b', а также их пересечение
# sa = set(a)
# sb = set(b)
# sa_and_sb = sa.intersection(sb)
#
# # Вывести уникальные элементы каждого списка и общие
# print("\nУникальные элементы:")
# print("1-й:", sa)
# print("2-й:", sb)
# print("общие:", sa_and_sb)
#
# # Соединить списки 'a' и 'b'
# c = a + b
#
# # Отсортировать список 'c' по возрастанию и убыванию
# c_asc = sorted(c)
# c_desc = sorted(c, reverse=True)
#
# # Среднее арифметическое элементов списка 'c', расположенных на четных местах
# even_elements = c[1::2]
# sr_ar = sum(even_elements) / len(even_elements)
#
# # Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
# import math
# odd_elements = c[0::2]
# sr_geom = math.prod(odd_elements) ** (1 / len(odd_elements))
#
# # Максимальный и минимальный элементы
# c_max = max(c)
# c_min = min(c)
#
# # Вывести результаты на экран
# print("\nИтоговые:")
# print("3-й:", c)
# print("Сортировка (возр.):", c_asc)
# print("Сортировка (убыв.):", c_desc)
# print(f"Ср. арифм. = {sr_ar:.2f}, ср. геометр. = {sr_geom:.2f}")
# print("Макс. и мин.:", c_max, c_min)


#Задача 14

# 1. Создание словаря
# Создать пустой словарь
info = {}

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = "Иванов Иван Иванович"
info["дата_рождения"] = "01/09/1995"
info["место_рождения"] = "Париж"

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк - наименований хобби
info["хобби"] = ["игра на гитаре", "туризм"]

# Добавить "программирование" в список хобби
info["хобби"].append("программирование")

# Создать ключ "животные" со значением = кортеж из строк - имен домашних животных
info["животные"] = ("кошка Мурка", "пес Барбос")

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info["ЕГЭ"] = {}

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах
info["ЕГЭ"]["Математика"] = 90
info["ЕГЭ"]["Информатика"] = 88
info["ЕГЭ"]["Русский язык"] = 67

# Добавить экзамен, который не был сдан, после чего удалить его
info["ЕГЭ"]["Химия"] = 0
del info["ЕГЭ"]["Химия"]

# Создать ключ "вузы" и поместить в него пустой словарь
info["вузы"] = {}

# В словарь info["вузы"] добавить информацию о вузах
info["вузы"]["МИРЭА"] = 240
info["вузы"]["МГУ"] = 295
info["вузы"]["МГТУ им. Баумана"] = 255

# 2. Вывод на экран
print("Данные:")
# Получившийся словарь
print(info)

# Список экзаменов ЕГЭ в алфавитном порядке
exams = tuple(sorted(info["ЕГЭ"].keys()))
print("Предметы:", exams)

# Список вузов в алфавитном порядке
uni = tuple(sorted(info["вузы"].keys()))
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info["фио"].split()[1]
# Начинается на гласную? (True/False)
starts_with_vowel = name[0].lower() in "аеёиоуыэюя"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
month = int(info["дата_рождения"].split("/")[1])
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = month in [12, 1, 2, 6, 7, 8]
print("* родился летом или зимой:", born_in_winter_or_summer)

# Количество хобби и первое из них
hobbies_count = len(info["хобби"])
print(f"* у меня {hobbies_count} хобби, первое \"{info['хобби'][0]}\"")

# Количество сданных экзаменов
print(f"* после окончания школы сдавал {len(info['ЕГЭ'])} экз.")

# Сумма баллов по экзаменам
sum_mark = sum(info["ЕГЭ"].values())
print(f"* сумма баллов = {sum_mark}")

# Максимальный балл среди сданных
max_mark = max(info["ЕГЭ"].values())
print(f"* макс. балл = {max_mark}")

# Количество вузов, в которые Вы проходите по баллам
vuz_count = sum(int(sum_mark >= passing_score) for passing_score in info["вузы"].values())
print(f"* кол-во вузов в которые прохожу: {vuz_count}")
