n = int(input('Input amout of numbers: '))
main_list = [int(input()) for i in range(n)]
counter = 0
for i in main_list:
    if i % 2 == 0:
        counter += 1
print(counter)