##Задача 1. Стек
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def remove_task(self, task, priority):
        if priority in self.tasks and not self.tasks[priority].is_empty():
            temp_stack = Stack()
            removed = False
            while not self.tasks[priority].is_empty():
                current_task = self.tasks[priority].pop()
                if current_task == task and not removed:
                    removed = True
                else:
                    temp_stack.push(current_task)
            while not temp_stack.is_empty():
                self.tasks[priority].push(temp_stack.pop())

    def __str__(self):
        result = []
        for priority in sorted(self.tasks):
            tasks_at_priority = []
            while not self.tasks[priority].is_empty():
                tasks_at_priority.append(self.tasks[priority].pop())
            result.append(f"{priority} " + "; ".join(reversed(tasks_at_priority)))
        return "\n".join(result)


# Пример использования:
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)

# Удалим задачу
manager.remove_task("поесть", 2)
print("\nПосле удаления задачи 'поесть':")
print(manager)


##Задача 2. Кэширование запросов
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    @property
    def cache(self):
        return list(self.cache.items())[0]

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache.items():
            print(f"{key} : {value}")


# Пример использования:
cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key4", "value4")
cache.print_cache()


##Задача 3. Кэширование для ускорения вычислений
def cache_decorator(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Пример использования:
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765



##Задача 4. Крестики нолики
class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.symbol = None

    def occupy(self, symbol):
        if not self.is_occupied:
            self.symbol = symbol
            self.is_occupied = True
            return True
        return False

    def __str__(self):
        return self.symbol if self.is_occupied else str(self.number)


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(0, 9, 3):
            print(" | ".join(str(self.cells[j]) for j in range(i, i + 3)))
            if i < 6:
                print("---------")

    def make_move(self, number, symbol):
        return self.cells[number - 1].occupy(symbol)

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.cells[combo[0]].symbol == self.cells[combo[1]].symbol == self.cells[combo[2]].symbol and self.cells[combo[0]].symbol:
                return self.cells[combo[0]].symbol
        return None

    def is_full(self):
        return all(cell.is_occupied for cell in self.cells)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                cell_number = int(input(f"{self.name}, выберите клетку (1-9): "))
                if 1 <= cell_number <= 9 and board.make_move(cell_number, self.symbol):
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except ValueError:
                print("Введите число от 1 до 9.")


def play_game():
    board = Board()
    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")
    current_player = player1

    while not board.is_full():
        board.display()
        current_player.make_move(board)

        winner = board.check_winner()
        if winner:
            board.display()
            print(f"Победитель: {winner}!")
            return

        current_player = player2 if current_player == player1 else player1

    board.display()
    print("Ничья!")


# Запуск игры
play_game()

