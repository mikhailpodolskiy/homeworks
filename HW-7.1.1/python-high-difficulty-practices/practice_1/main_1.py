import pandas as pd

def read_file(): # Функция чтения данных из файла
    df = pd.read_csv('cafe_expenses_extended.csv')
    return df

print(read_file())

def max_avg(): # Вычисление общей суммы расходов и средний расход по каждой категории
    matrix = []
    for i in range(len(read_file().index)):
        matrix.append([])
        for j in range(2):
            if j == 0:
                matrix[i].append(f"Сумма расходов в категории {read_file().iloc[i, 0]}, равна {read_file().iloc[i, 1:].sum()} рублей")
            else:
                matrix[i].append(f"Средний расход в категории {read_file().iloc[i, 0]}, равно {read_file().iloc[i, 1:].mean()} рублей")
    return matrix

print(max_avg())

def write_to_file(): #	Функция записи данных в файл
    with open('cafe_expenses_extended_report.txt', 'w') as f:
        for row in max_avg():
            for elem in row:
                f.write(elem + '\n')
    f.close
    return "Файл успешно записан"

print(write_to_file())
