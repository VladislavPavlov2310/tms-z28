from random import randint

n = int(input('Input n: '))
matrix = [[randint(0, 10) for i in range(n)] for j in range(n)]
for i in range(n):
    print(matrix[i])
print('\n')
jmax = 0
for i in range(n):
    max_in_row = matrix[i][0]
    for j in range(n):
        if matrix[i][j] >= max_in_row:
            max_in_row = matrix[i][j]
            jmax = j
    tmp = matrix[i][jmax]
    matrix[i][jmax] = matrix[i][i]
    matrix[i][i] = tmp
for i in range(n):
    print(matrix[i])
