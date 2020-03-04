from decimal import Decimal
n = int(input('Input number: '))
summ = 0
for i in range(1, n + 1):
    summ += Decimal(1 / i)
    print(f'{i})sum: {summ}, element: 1 / {i}')
