from random import randint
n = int(input('Input n: '))
array = [randint(0, 20) for i in range(n)]
print(array)
aux_list = []
counter = 0
i = 0
for j in range(n-1):
    while array[j + 1] >= array[j]:
        j += 1
    aux_list.append(array[i:j + 1])
    i = j + 1
    j += 1
for i in aux_list:
    if len(i) >= 2:
        counter += 1
print(counter)
