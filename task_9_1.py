string_list = input('Input string: ').split(' ')
string_list = [f'{i} - {line}' for i, line in enumerate(string_list)]
print(string_list)
