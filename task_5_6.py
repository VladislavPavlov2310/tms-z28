from random import randint

n = int(input('Input n: '))
array = [randint(0, 20) for i in range(n)]
print(array)
aux_list = [[array[0]]]
counter = 0
j = 0
for i in range(1, n):
    if array[i] > aux_list[j][-1]:
        aux_list[j].append(array[i])
    else:
        j += 1
        aux_list.append([array[i]])
print(aux_list)
for i in aux_list:
    if len(i) > 1:
        counter += 1
print(counter)
