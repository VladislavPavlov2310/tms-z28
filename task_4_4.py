main_list = [1, 2, 3, 4, 5]
sec_list = main_list.copy()
sec_list.append(sec_list.pop(0))
print(sec_list)
