import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Установка относительного пути к файлу данных
data_file = os.path.join(os.path.dirname(__file__), 'dataset.csv')

# Установка шрифта для поддержки кириллицы
plt.rcParams['font.family'] = 'DejaVu Sans'

# 1. Создание массивов
array_1d = np.arange(10)  # Одномерный массив от 0 до 9
array_2d = np.random.randint(1, 11, (3, 3))  # Двумерный массив 3x3 со случайными числами от 1 до 10

# 2. Операции с массивами
array_add = array_1d + 2
array_sub = array_1d - 2
array_mul = array_1d * 2
array_div = array_1d / 2
dot_product = np.dot(array_1d, array_1d)

# 3. Индексация и срезы
second_third_elements = array_1d[1:3]
first_row = array_2d[0, :]
last_column = array_2d[:, -1]
elements_greater_5 = array_2d[array_2d > 5]
array_2d[:, 0] = 0  # Замена первого столбца на 0
diagonal_elements = np.diag(array_2d)

# 4. Статистика
mean_value = np.mean(array_1d)
median_value = np.median(array_1d)
std_deviation = np.std(array_1d)
max_value_2d = np.max(array_2d)
min_value_2d = np.min(array_2d)
max_index = np.unravel_index(np.argmax(array_2d), array_2d.shape)
min_index = np.unravel_index(np.argmin(array_2d), array_2d.shape)

# 5. Изменение формы и транспонирование
array_reshaped = array_1d.reshape(2, 5)
array_transposed = array_reshaped.T

# 6. Булева индексация
bool_mask = (array_2d % 2 == 0)
even_elements = array_2d[bool_mask]
array_2d[array_2d < 5] = -1  # Замена элементов меньше 5 на -1

# 7. Работа с Pandas
try:
    # Попытка загрузить данные с указанием кодировки для корректного отображения кириллицы
    df = pd.read_csv(data_file, on_bad_lines='skip', delimiter=';', encoding='utf-8-sig')

    # Задание 1: Загрузка данных и анализ
    print(df.head())  # Первые 5 строк
    print(df.info())  # Общая информация
    print(df.describe())  # Статистическое описание

    # Задание 2: Очистка данных
    df['use_meters'] = pd.to_numeric(df['use_meters'], errors='coerce')  # Преобразование в числовой формат
    df['use_meters'] = df['use_meters'].fillna(df['use_meters'].mean())  # Заполнение пропусков средним значением
    df['use_country'] = df['use_country'].fillna('Unknown')  # Заполнение "Unknown"
    df.drop_duplicates(inplace=True)  # Удаление дубликатов

    # Задание 3: Анализ
    records_per_year = df.groupby('year').size()  # Количество записей по годам
    print(records_per_year)

    top_agencies = df['state_agency'].value_counts().head(5)  # Топ-5 агентств
    print(top_agencies)

    # Анализ по типу использования
    meters_per_type = df.groupby('use_type')['use_meters'].sum().sort_values(ascending=False)
    print(meters_per_type)

    # Графики
    plt.figure(figsize=(12, 6))  # Увеличиваем размер графика
    records_per_year.plot(kind='bar', title='Количество записей по годам', color='skyblue')
    plt.xlabel('Год')
    plt.ylabel('Количество записей')
    plt.tight_layout(pad=1.5)
    plt.show()

    plt.figure(figsize=(12, 6))  # Увеличиваем размер графика
    top_agencies.plot(kind='bar', title='Топ-5 государственных агентств', color='lightgreen')
    plt.xlabel('Государственное агентство')
    plt.ylabel('Количество записей')
    plt.tight_layout(pad=1.5)
    plt.show()

    plt.figure(figsize=(14, 8))  # Увеличиваем размер графика для улучшения читаемости
    meters_per_type.head(10).plot(kind='barh', title='Общее количество метров по типам использования (Топ-10)', color='salmon')
    plt.xlabel('Общее количество метров')
    plt.ylabel('Тип использования')
    plt.tight_layout(pad=2.0)  # Увеличиваем отступы
    plt.show()

    # Задание 4: Группировка и агрегация
    pivot_table = df.pivot_table(index='year', columns='state_agency', values='use_meters', aggfunc='sum')
    print(pivot_table)

    top_positions = df['position'].value_counts().head(5)  # Топ-5 должностей
    average_meters = df[df['position'].isin(top_positions.index)].groupby('position')['use_meters'].mean()
    print(average_meters)

except FileNotFoundError:
    print(f"Ошибка: Файл {data_file} не найден. Убедитесь, что он находится в той же директории, что и скрипт.")
except pd.errors.ParserError as e:
    print(f"Ошибка чтения CSV-файла: {e}")
