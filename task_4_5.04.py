from random import randint
from decimal import Decimal
n = int(input('n: '))
m = int(input('m: '))
average_v = 0
matrix = [[randint(0, 10) for i in range(n)] for j in range(m)]
print(matrix)
for i in range(m):
    for elem in matrix[i]:
        average_v += elem
average_v  = Decimal(average_v / (n * m))
print(f'Average value: {average_v}')
counter = 0
for i in range(m):
    for j, elem in enumerate(matrix[i]):
        if (elem > average_v) & ((i + j) % 2 == 0):
            counter += 1
print(f'Counter: {counter}')


