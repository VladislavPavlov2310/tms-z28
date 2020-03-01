n = int(input('Input amount of numbers: '))
main_list = [int(input()) for i in range(n)]
sec_list = []
for i in main_list:
    sec_list.append(i * -2)
print(sec_list)


