##Задача 1
import math
from functools import reduce

# функция для нахождения НОД для списка чисел
def find_gcd(numbers):
    return reduce(math.gcd, numbers)

# функция для нахождения НОК для списка чисел
def find_lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers)

numbers = [12, 15, 20]
print("НОД:", find_gcd(numbers))
print("НОК:", find_lcm(numbers))

##Задача 2
import re

def count_sentences_with_digits(sentences):
    return sum(1 for sentence in sentences if re.search(r'\d', sentence))

sentences = ["Привет 2023!", "Это тест.", "123 - это число."]
print("Количество предложений с цифрами:", count_sentences_with_digits(sentences))


##Задача 3
def draw_frame(text, char):
    length = len(text) + 4
    print(char * length)
    print(f"{char} {text} {char}")
    print(char * length)

draw_frame("Текст в рамке", "*")


##Задача 4
from collections import Counter

def char_statistics(sentence):
    sentence = sentence.lower()
    stats = Counter(filter(str.isalpha, sentence))
    for char, count in stats.items():
        print(f"{char} = {count}")

char_statistics("Пример предложения для подсчета.")


##Задача 5
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if 'а' <= char <= 'я':
            new_char = chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
            encrypted_text += new_char
        elif 'А' <= char <= 'Я':
            new_char = chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

text = "Пример текста"
shift = 3
encrypted = caesar_cipher(text, shift)
print("Зашифровано:", encrypted)
print("Расшифровано:", caesar_cipher(encrypted, -shift))


##Задача 6
def separate_and_sort(*args):
    negative = sorted([x for x in args if x < 0], reverse=True)
    non_negative = sorted([x for x in args if x >= 0])
    return (negative, non_negative)

print(separate_and_sort(-1, 3, -5, 2, 0, -8))


##Задача 7
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

text = input("Введите строку: ")
if is_palindrome(text):
    print("Это палиндром")
else:
    print("Это не палиндром")


##Задача 8
def guess_number():
    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        print(f"Твое число равно, меньше или больше, чем {guess}? (1 - равно, 2 - больше, 3 - меньше)")
        response = int(input())
        attempts += 1

        if response == 1:
            print(f"Число угадано за {attempts} попыток!")
            return
        elif response == 2:
            low = guess + 1
        elif response == 3:
            high = guess - 1


guess_number()


##Задача 9
def to_decimal(number, base_from):
    return int(number, base_from)

def from_decimal(number, base_to):
    chars = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = chars[number % base_to] + result
        number //= base_to
    return result or "0"

def convert_number(number, base_from, base_to):
    if not (2 <= base_from <= 16 and 2 <= base_to <= 16):
        return "Ошибка: неподдерживаемая система счисления"
    decimal = to_decimal(number, base_from)
    return from_decimal(decimal, base_to)

print(convert_number("1010", 2, 16)) # Пример: 1010 из 2 в 16



##Задача 10
def is_magic_date(day, month, year):
    return day * month == year % 100

def find_magic_dates():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    if is_magic_date(day, month, year):
                        print(f"{day:02d}/{month:02d}/{year} - магическая дата")
                except ValueError:
                    continue

find_magic_dates()
