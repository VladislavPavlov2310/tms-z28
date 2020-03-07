from random import randint
from copy import deepcopy

# tasks: 9, 10
n = int(input('Input n:'))
main_matrix = [[randint(1, 20) for i in range(n)] for j in range(n)]
matrix_lower = deepcopy(main_matrix)
matrix_upper = deepcopy(main_matrix)
for i in main_matrix:
    print(i)

for i in range(n):
    for j in range(i + 1, n):
        matrix_upper[i][j] = 0
print('Zeros upper the main diagonal')
for i in matrix_upper:
    print(i)

for i in range(n):
    for j in range(i + 1, n):
        matrix_lower[j][i] = 0
print('Zeros lower the main diagonal')
for i in matrix_lower:
    print(i)

# tasks: 11, 12, 13, 14
n = int(input('Input n:'))
m = int(input('Input m:'))
matrix_a = [[randint(1, 20) for i in range(n)] for j in range(m)]
matrix_b = [[randint(1, 20) for i in range(n)] for j in range(m)]
print('Matrix A:')
for i in matrix_a:
    print(i)
print('Matrix B:')
for i in matrix_b:
    print(i)

matrix_sum = [[matrix_a[j][i] + matrix_b[j][i] for i in range(n)] for j in range(m)]
print('Sum result:')
for i in matrix_sum:
    print(i)
matrix_diff = [[matrix_a[j][i] - matrix_b[j][i] for i in range(n)] for j in range(m)]
print('Difference result:')
for i in matrix_diff:
    print(i)

multiplier = int(input('Input multiplier:'))
matrix_multiply = [[matrix_a[j][i] * multiplier for i in range(n)] for j in range(m)]
print('Multiply result:')
for i in matrix_diff:
    print(i)
