import pandas as pd


def calculate_mode(row):
    counts = {}
    
    for value in row:
        counts[value] = counts.get(value, 0) + 1
    
    max_count = max(counts.values())
    mode_values = [key for key, value in counts.items() if value == max_count]
    
    return mode_values



def calculate_median(row):
    sorted_values = sorted(row)
    n = len(sorted_values)
    
    if n % 2 == 0:
        median_value = (sorted_values[n // 2] + sorted_values[n // 2 - 1]) / 2
    else:
        median_value = sorted_values[n // 2]
    
    return median_value



file_name = "Задание 2.xlsx"
print("расчитать моду и медиану")

xl = pd.ExcelFile(file_name)

task56 = xl.parse("Таблица 2")

task56['mode'] = task56[['неуд', 'удовл', 'хорошо', 'отлично']].apply(lambda row: calculate_mode(row)[0], axis=1)
# task5['mode'] = task56[['неуд', 'удовл', 'хорошо', 'отлично']].apply(lambda row: row.mode()[0], axis=1)
task56['median'] = task56[['неуд', 'удовл', 'хорошо', 'отлично']].apply(calculate_median, axis=1)
# task56['median'] = task56[['неуд', 'удовл', 'хорошо', 'отлично']].median(axis=1)
print(task56)

