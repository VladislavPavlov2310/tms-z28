guests = int(input('How many guests are invited: '))
if guests > 50:
    print('The wedding will be in a restaurant!')
elif guests > 20 and guests <=50:
    print('The wedding will be in a cafe!')
elif guests <=20:
    print('The wedding will be in at home!')