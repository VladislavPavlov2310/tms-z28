from decimal import Decimal
x_num = Decimal(input('Input X: '))
y_num = Decimal(input('Input Y: '))
op_list = ['+', '-', '/', '*', '0']
while True:
    operation = ''
    while operation not in op_list:
        operation = input('Choose operation (+, -, *, /): ')
    if operation == '+':
        print(x_num + y_num)
    elif operation == '-':
        print(x_num - y_num)
    elif operation == '*':
        print(x_num * y_num)
    elif operation == '/':
        while y_num == 0:
            print('Division by zero!')
            y_num = Decimal(input('Input Y: '))
        print(x_num / y_num)
    else: break

