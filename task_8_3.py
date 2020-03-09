def exp_in_row(x, eps):
    n = 0
    summ_func = 0
    while True:
        fact = 1
        for i in range(2 * n + 1, 0, -1):
            fact *= i
        temp = pow(-1, n) * pow(x, 2 * n + 1) / fact
        if abs(temp) > eps:
            summ_func += temp
        else:
            break
        n += 1
    return summ_func


x_func = float(input('Input x in function sin(x): '))
eps_func = [float(input(f'Input epsilon {i + 1}: ')) for i in range(6)]
for epsilon in eps_func:
    print(f'To epsilon {epsilon}: {exp_in_row(x_func, epsilon)}')
