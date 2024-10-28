## Задача 1.
# Основной список
a = [1, 5, 3]

# Побочные списки
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

# Добавляем элементы из списка b в основной список a
a.extend(b)

# Считаем количество цифр 5
count_5 = a.count(5)
print(f"Кол-во цифр 5 при первом объединении: {count_5}")

# Удаляем все пятёрки из основного списка
a = [x for x in a if x != 5]

# Добавляем элементы из списка c в основной список a
a.extend(c)

# Считаем количество цифр 3
count_3 = a.count(3)
print(f"Кол-во цифр 3 при втором объединении: {count_3}")

# Выводим итоговый список
print(f"Итоговый список: {a}")

## Задача 2.
class1_heights = list(range(160, 177, 2))
class2_heights = list(range(162, 181, 3))

combined_heights = sorted(class1_heights + class2_heights)
print("Отсортированный список учеников:", combined_heights)

## Задача 3.
shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500], ['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]

detail = input("Название детали: ").strip()
quantity = sum(1 for item in shop if item[0] == detail)
total_cost = sum(item[1] for item in shop if item[0] == detail)

print(f"Кол-во деталей — {quantity}")
print(f"Общая стоимость — {total_cost}")

## Задача 4.
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
max_guests = 6

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек:", guests)
    action = input("Гость пришёл или ушёл? ").strip().lower()
    if action == "пора спать":
        break
    name = input("Имя гостя: ").strip()

    if action == "пришёл":
        if len(guests) < max_guests:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif action == "ушёл":
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}!")

print("Вечеринка закончилась, все легли спать.")


## Задача 5
violator_songs = [
    ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56], ['Halo', 4.9],
    ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83]
]

num_songs = int(input("Сколько песен выбрать? "))
selected_songs = [input(f"Название {i + 1}-й песни: ").strip() for i in range(num_songs)]
total_duration = sum(song[1] for song in violator_songs if song[0] in selected_songs)

print(f"Общее время звучания песен: {total_duration:.2f} минуты")


## Задача 6
first_list = [int(input(f"Введите {i+1}-е число для первого списка: ")) for i in range(3)]
second_list = [int(input(f"Введите {i+1}-е число для второго списка: ")) for i in range(7)]

first_list.extend(second_list)
unique_first_list = list(set(first_list))

print("Новый первый список с уникальными элементами:", unique_first_list)


## Задача 7
n = int(input("Кол-во коньков: "))
skates = sorted([int(input(f"Размер {i + 1}-й пары: ")) for i in range(n)], reverse=True)

k = int(input("Кол-во людей: "))
feet = sorted([int(input(f"Размер ноги {i + 1}-го человека: ")) for i in range(k)], reverse=True)

count = 0
for foot in feet:
    for i in range(len(skates)):
        if skates[i] >= foot:
            count += 1
            skates.pop(i)
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", count)


## Задача 8
n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))

people = list(range(1, n + 1))
index = 0

while len(people) > 1:
    index = (index + k - 1) % len(people)
    print("Выбывает человек под номером", people[index])
    people.pop(index)

print("Остался человек под номером", people[0])


## Задача 9
n = int(input("Кол-во друзей: "))
k = int(input("Долговых расписок: "))

balance = [0] * n
for i in range(k):
    debtor = int(input("Кому: ")) - 1
    creditor = int(input("От кого: ")) - 1
    amount = int(input("Сколько: "))
    balance[debtor] -= amount
    balance[creditor] += amount

print("Баланс друзей:")
for i, b in enumerate(balance, 1):
    print(f"{i}: {b}")


## Задача 9
n = int(input("Кол-во чисел: "))
sequence = [int(input("Число: ")) for _ in range(n)]

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        extra_numbers = sequence[:i][::-1]
        print("Нужно приписать чисел:", len(extra_numbers))
        print("Сами числа:", extra_numbers)
        break


## Задача 10
n = int(input("Кол-во чисел: "))
sequence = [int(input("Число: ")) for _ in range(n)]

for i in range(len(sequence)):
    if sequence[i:] == sequence[i:][::-1]:
        extra_numbers = sequence[:i][::-1]
        print("Нужно приписать чисел:", len(extra_numbers))
        print("Сами числа:", extra_numbers)
        break


