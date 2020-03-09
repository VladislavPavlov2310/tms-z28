def double_factorial(number):
    temp = 1
    for i in range(number, 0, -2):
        temp *= i
    return temp


factorial_list = [int(input('Input number: ')) for i in range(5)]
aux_list = [double_factorial(num) for num in factorial_list]
print(aux_list)
