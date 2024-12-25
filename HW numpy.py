import numpy as np

# Создание массивов
array_1d = np.random.randint(1, 101, 10)  # Одномерный массив из 10 случайных целых чисел (1-100)
array_2d = np.random.rand(5, 5)  # Двумерный массив 5x5 с числами от 0 до 1
array_linspace = np.linspace(0, 5, 20)  # 20 равномерно распределенных чисел между 0 и 5
array_reshaped = np.arange(1, 21).reshape(4, 5)  # Преобразование одномерного массива в 4x5

# Базовые операции
print("Суммы элементов:", array_1d.sum(), array_2d.sum(), array_linspace.sum(), array_reshaped.sum())
print("Средние значения:", array_1d.mean(), array_2d.mean(), array_linspace.mean(), array_reshaped.mean())
print("Макс/мин значения:")
print("array_1d:", array_1d.max(), array_1d.min())
print("array_2d:", array_2d.max(), array_2d.min())
print("array_linspace:", array_linspace.max(), array_linspace.min())
print("array_reshaped:", array_reshaped.max(), array_reshaped.min())


# Выбор элементов больше 50 из одномерного массива
elements_gt_50 = array_1d[array_1d > 50]

# Элементы в четных строках и нечетных столбцах (индексация 0-based)
elements_2d = array_2d[::2, 1::2]

# Элементы с 3 по 7 индекс
elements_3_7 = array_1d[3:8]

# Подмассив 3x3 начиная с (1,1)
subarray_3x3 = array_2d[1:4, 1:4]

print("Элементы > 50:", elements_gt_50)
print("Четные строки, нечетные столбцы:", elements_2d)
print("Элементы с 3 по 7 индекс:", elements_3_7)
print("Подмассив 3x3:", subarray_3x3)


# Создание массивов
array_a = np.random.rand(10)
array_b = np.random.rand(10)

# Поэлементные операции
sum_arrays = array_a + array_b
sub_arrays = array_a - array_b
mul_arrays = array_a * array_b
div_arrays = array_a / array_b

# Скалярное произведение
dot_product = np.dot(array_a, array_b)

print("Сумма:", sum_arrays)
print("Разность:", sub_arrays)
print("Умножение:", mul_arrays)
print("Деление:", div_arrays)
print("Скалярное произведение:", dot_product)

# Создание матриц
matrix_a = np.random.randint(1, 10, (3, 3))
matrix_b = np.random.randint(1, 10, (3, 3))

# Матричное умножение
matrix_mult = np.matmul(matrix_a, matrix_b)

# Обратная матрица
matrix_inverse = np.linalg.inv(matrix_a)

print("Матрица A:", matrix_a)
print("Матрица B:", matrix_b)
print("Произведение матриц:", matrix_mult)
print("Обратная матрица:", matrix_inverse)


# Создание массива (имен клиентов, возрастов, стоимости ремонта)
clients_data = np.array([
    ["Alice", 30, 500],
    ["Bob", 45, 300],
    ["Charlie", 25, 700],
    ["Diana", 35, 400],
    ["Eve", 40, 1000]
], dtype=object)

# Сортировка по возрасту (2-й столбец)
clients_sorted = clients_data[clients_data[:, 1].astype(int).argsort()]

# Средние значения возраста и стоимости ремонта
average_age = clients_data[:, 1].astype(int).mean()
average_cost = clients_data[:, 2].astype(int).mean()

# Клиент с максимальной стоимостью ремонта
max_cost_idx = clients_data[:, 2].astype(int).argmax()
client_max_cost = clients_data[max_cost_idx]

print("Сортировка по возрасту:\n", clients_sorted)
print("Средний возраст:", average_age)
print("Средняя стоимость ремонта:", average_cost)
print("Клиент с максимальной стоимостью ремонта:", client_max_cost)
