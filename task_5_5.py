from random import randint
array = [randint(0, 100) for i in range(19)]
max_elem = max(array)
print(array)
print(f'max element: {max_elem}')
for i in range(19):
    if array[i] % 2 == 0:
        array[i] = max_elem
print(array)