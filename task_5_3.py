main_list = []
friend_list = []
for elem in range(200, 301):
    num_1 = elem - 1
    while num_1:
        if elem % num_1 == 0:
            main_list.append(num_1)
        num_1 -= 1
    total_1 = sum(main_list)
    main_list.clear()
    if 200 <= total_1 <= 300:
        num_2 = total_1 - 1
        while num_2:
            if total_1 % num_2 == 0:
                main_list.append(num_2)
            num_2 -= 1
        total_2 = sum(main_list)
        if total_2 == elem:
            friend_list.append([total_1, total_2])
print(friend_list)
