a = list(input('Write number: '))
print(a)
summ = 0
prod = 1
for i in a:
    summ += int(i)
    prod *= int(i)
print(f'sum {summ}, prod {prod}')
