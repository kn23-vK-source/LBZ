import csv
import pandas as pd
from datetime import datetime

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data_list = []
        for row in csv_reader:
            row['Дата народження'] = datetime.strptime(row['Дата народження'], '%Y-%m-%d')
            row['вік'] = (datetime.now() - row['Дата народження']).days // 360
            data_list.append(row)
    return data_list

csv_file = 'data.csv'
data_list = read_csv(csv_file)

df = pd.DataFrame(data_list)
df = df[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'вік']]

output_file = 'output.xlsx'
with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, sheet_name='all', index=False)

    younger_18 = df[df['вік'] < 18]
    younger_18.to_excel(writer, sheet_name='younger_18', index=False)

    age_18_45 = df[(df['вік'] >= 18) & (df['вік'] <= 45)]
    age_18_45.to_excel(writer, sheet_name='18-45', index=False)

    age_45_70 = df[(df['вік'] > 45) & (df['вік'] <= 70)]
    age_45_70.to_excel(writer, sheet_name='45-70', index=False)

    older_70 = df[df['вік'] > 70]
    older_70.to_excel(writer, sheet_name='older_70', index=False)

print(f"Дані успішно записані у файл {output_file}")