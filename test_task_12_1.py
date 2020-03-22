from task_12_1 import MyTime

time_1 = MyTime(25, 66, 13)
time_2 = MyTime('23 54 11')
time_3 = MyTime(time_1)
time_4 = MyTime()
print(f'{time_1}\n{time_2}\n{time_3}\n{time_4}')

print(f'time_1 < time_2: {time_1 < time_2}')
print(f'time_1 <= time_3: {time_1 <= time_3}')
print(f'time_1 > time_2: {time_1 > time_2}')
print(f'time_1 != time_2: {time_1 < time_2}')
print(f'time_1 + time_2: {time_1 + time_2}')
print(f'time_2 - time_3: {time_2 - time_3}')
print(f'time_1 * 3: {time_1 * 3}')
