## Задача 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


##Задача 2
class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def area(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return width * height

    def perimeter(self):
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return 2 * (width + height)


##Задача 3
    def contains(self, point):
        return (self.bottom_left.x <= point.x <= self.top_right.x and
                self.bottom_left.y <= point.y <= self.top_right.y)


##Задача 4
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

    def get_counter(self):
        return self.value


##Задача 5
class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def add_hour(self):
        self.hours = (self.hours + 1) % 24

    def add_minute(self):
        self.minutes = (self.minutes + 1) % 60
        if self.minutes == 0:
            self.add_hour()

    def add_second(self):
        self.seconds = (self.seconds + 1) % 60
        if self.seconds == 0:
            self.add_minute()


##Задача 6
    def __add__(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return Clock(hours, minutes, seconds)


##Задача 7
class Grass:
    def __init__(self, nutrition_value):
        self.nutrition_value = nutrition_value

class Herbivore:
    def __init__(self, hunger):
        self.hunger = hunger

    def eat(self, grass):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - grass.nutrition_value)
            return "Eating grass"
        return "Not hungry"


##Задача 8
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Storm):
            return Energy()  # Дополнительный элемент
        return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        return None


# Классы для результирующих элементов
class Storm:
    def __str__(self):
        return "Шторм"


class Steam:
    def __str__(self):
        return "Пар"


class Mud:
    def __str__(self):
        return "Грязь"


class Lightning:
    def __str__(self):
        return "Молния"


class Dust:
    def __str__(self):
        return "Пыль"


class Lava:
    def __str__(self):
        return "Лава"


# Дополнительный элемент
class Energy:
    def __str__(self):
        return "Энергия"


# Пример использования
if __name__ == "__main__":
    water = Water()
    air = Air()
    fire = Fire()
    earth = Earth()
    storm = Storm()

    print(water + air)  # Шторм
    print(water + fire)  # Пар
    print(water + earth)  # Грязь
    print(air + fire)  # Молния
    print(air + earth)  # Пыль
    print(fire + earth)  # Лава
    print(fire + storm)  # Энергия
    print(water + storm)  # None (не определено)

##Задача 9
class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)

def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))

def transfer_money(accounts, account_from, account_to, value):
    """Выполнить перевод 'value' денег со счета 'account_from' на 'account_to'.

    При переводе денежных средств необходимо учитывать:
        - хватает ли денег на счету, с которого осуществляется перевод;
        - перевод состоит из уменьшения баланса первого счета и увеличения
          баланса второго; если хотя бы на одном этапе происходит ошибка,
          аккаунты должны быть приведены в первоначальное состояние
          (механизм транзакции)
    Исключения (raise):
        - NoMoneyToWithdrawError: на счету 'account_from'
                                  не хватает денег для перевода;
        - PaymentError: ошибка при переводе.
    """
    try:
        # Проверка наличия счетов
        if account_from not in accounts or account_to not in accounts:
            raise KeyError("Один из указанных счетов не найден.")

        # Проверка наличия достаточных средств
        if accounts[account_from] < value:
            raise NoMoneyToWithdrawError(f"Недостаточно средств на счете '{account_from}' для перевода.")

        # Транзакция: сохранение начальных значений
        initial_from_balance = accounts[account_from]
        initial_to_balance = accounts[account_to]

        # Проведение перевода
        accounts[account_from] -= value
        accounts[account_to] += value

    except NoMoneyToWithdrawError as e:
        print(f"Ошибка перевода: {e}")
    except KeyError as e:
        print(f"Ошибка перевода: {e}")
    except Exception as e:
        # Откат транзакции в случае любой другой ошибки
        accounts[account_from] = initial_from_balance
        accounts[account_to] = initial_to_balance
        raise PaymentError("Произошла ошибка при переводе средств") from e

if __name__ == "__main__":
    accounts = {
        "Василий Иванов": 100,
        "Екатерина Белых": 1500,
        "Михаил Лермонтов": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Екатерина Белых",
        "account_to": "Василий Иванов"
    }

    print("Перевод от {account_from} для {account_to}...".format(**payment_info))

    try:
        payment_info["value"] = int(input("Сумма = "))
        transfer_money(accounts, **payment_info)
        print("OK!")
    except ValueError:
        print("Ошибка: сумма должна быть числом.")

    print_accounts(accounts)


## Задача 10
def sum_numbers():
    total_sum = 0.0
    while True:
        user_input = input("Введите число (или нажмите Enter для завершения): ")

        # Завершение программы при пустом вводе
        if user_input == "":
            print("Программа завершена.")
            break

        try:
            # Преобразование ввода в число
            number = float(user_input)
            total_sum += number
            print(f"Текущая сумма: {total_sum}")

        except ValueError:
            # Сообщение о некорректном вводе
            print("Введенное значение не является числом. Попробуйте еще раз.")


# Запуск функции
sum_numbers()


