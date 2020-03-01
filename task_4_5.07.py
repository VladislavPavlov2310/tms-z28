from random import randint
while True:
    while True:
        n = int(input('Input left limit: '))
        m = int(input('Input right limit: '))
        if n < m:
            break
        print('Left limit should be less than right limit!')

    attempts = int(input('Amount of try: '))
    num_to_gues = randint(n, m)
    player_try = 0
    for i in range(attempts):
        player_try = int(input('Your number is: '))
        if player_try > num_to_gues:
            print(f'Incorrect! Right number is smaller than yours! \n{attempts - i - 1} attempt(s) left!')
        elif player_try < num_to_gues:
            print(f'Incorrect! Right number is bigger than yours! \n {attempts - i - 1} attempt(s) left!')
        else:
            print(f'Correct! You are the winner)')
            break

    if player_try != num_to_gues:
        print(f'You lose! So sad! That is right number - {num_to_gues}\nYou were near to win) Try again!')
    if input('Do you want to play again? (Y/N):') == 'N':
        break




