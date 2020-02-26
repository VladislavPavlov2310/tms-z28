main_str = input('Input string, please: ')
central_index  = int(len(main_str)/2)
print(main_str[central_index])
if main_str[central_index] == main_str[0]:
    sec_str = main_str[1:-1]
    print(sec_str)


