from datetime import timedelta, datetime

train_dict = [
    {
        'train': '1',
        'way_to': 'Berlin',
        'time_to': '01/02/2020 06:06',
        'way_from': 'Moscow',
        'time_from': '01/01/2020 09:56'
    },
    {
        'train': '2',
        'way_to': 'Vitebsk',
        'time_to': '01/02/2020 00:50',
        'way_from': 'Saint-Petersburg',
        'time_from': '01/01/2020 16:10'
    },
    {
        'train': '3',
        'way_to': 'Helsinki',
        'time_to': '01/02/2020 17:57',
        'way_from': 'Minsk',
        'time_from': '01/01/2020 19:52'
    },
    {
        'train': '4',
        'way_to': 'Saint-Petersburg',
        'time_to': '01/01/2020 17:25',
        'way_from': 'Moscow',
        'time_from': '01/01/2020 13:30'
    }
]

for i in train_dict:
    time_to = datetime.strptime(i['time_to'], '%m/%d/%Y %H:%M')
    time_from = datetime.strptime(i['time_from'], '%m/%d/%Y %H:%M')
    raz = time_to - time_from
    if raz.seconds > 26400:
        print(i)
        print(f'Time difference: {raz}')
