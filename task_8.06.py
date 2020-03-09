while True:
    print('Input A, B, C in quadratic equation:')
    A = float(input('A: '))
    B = float(input('B: '))
    C = float(input('C: '))
    print(f'Your equation: {A} x^2 + {B} x + {C} = 0\n')
    D = (B ** 2) - (4 * A * C)
    if D > 0:
        x1 = (-B + (D ** (1 / 2))) / 2 * A
        x2 = (-B - (D ** (1 / 2))) / 2 * A
        print(f'x1 = {x1}\nx2 = {x2}\n')
    elif D == 0:
        x1 = -B / 2 * A
        print(f'x1 = x2 = {x1}\n')
    else:
        print(f'x1 = {-B / 2 * A} + {(abs(D) ** (1 / 2)) / 2 * A} j')
        print(f'x1 = {-B / 2 * A} - {(abs(D) ** (1 / 2)) / 2 * A} j\n')
    if input('Do you want to continue? (y/n): ') == 'n':
        break
