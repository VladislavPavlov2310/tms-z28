n = int(input('Write n: '))
m = int(input('Write m: '))
main_list = []
for i in range(n, m + 1):
    num = i
    temp = num - 1
    while temp - 1:
        if num % temp == 0:
            main_list.append(temp)
        temp -= 1
    print(f'For {num}: {main_list}')
    main_list.clear()


