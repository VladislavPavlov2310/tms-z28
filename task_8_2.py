def if_palindrome(word):
    if word == word[::-1]:
        print(f'{word} -> YES')
    else:
        print(f'{word} -> NO')


check_string = (input('Input string: ')).split(' ')
for elem in check_string:
    if_palindrome(elem)
