import csv

average_degrees = 0
average_wind_speed = 0
with open('task_2_daily_weather.csv', 'r') as file_weather:
    main_list = list(filter(lambda x: x[1] == 'Minsk', list(csv.reader(file_weather))[1::]))
for obj in main_list[len(main_list):len(main_list) - 8:-1]:
    average_degrees += int(obj[2])
    average_wind_speed += int(obj[3])
print(f'Average temperature and wind speed in last 7 days:\n'
      f'{average_degrees / 7} *C, {average_wind_speed / 7} km/h')
