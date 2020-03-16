import csv
from datetime import datetime

with open('task_3_dates.csv', 'r') as file_dates:
    date_reader = list(csv.reader(file_dates))[1::]
date_list = [datetime.strptime('/'.join(i), '%d/%m/%Y') for i in date_reader]

print(f'The earliest date: {min(date_list)}')
