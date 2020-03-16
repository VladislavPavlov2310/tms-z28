import csv

dct = {
    '1-12': 0,
    '13-18': 0,
    '19-25': 0,
    '26-40': 0,
    '40+': 0
}
with open('task_1_structure.csv', 'r') as file_struct:
    with open('task_1_report.csv', 'w') as file_report:
        reader_struct = csv.reader(file_struct)
        writer_rep = csv.DictWriter(file_report, fieldnames=['1-12', '13-18', '19-25', '26-40', '40+'])
        writer_rep.writeheader()
        for row in list(reader_struct)[1::]:
            if int(row[2]) < 13:
                dct['1-12'] += 1
            elif int(row[2]) < 19:
                dct['13-18'] += 1
            elif int(row[2]) < 25:
                dct['19-25'] += 1
            elif int(row[2]) < 40:
                dct['26-40'] += 1
            else:
                dct['40+'] += 1
        writer_rep.writerow(dct)
