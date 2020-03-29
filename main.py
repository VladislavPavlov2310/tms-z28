import classes
from decimal import Decimal, InvalidOperation
from exceptions import ChoiceException

math_obj = classes.Math()
while True:
    while True:
        try:
            num1 = Decimal(input('Input firs number: '))
            num2 = Decimal(input('Input second number: '))
            math_obj.num1 = num1
            math_obj.num2 = num2
            break
        except NameError:
            print('Write numbers, please!\n')
        except InvalidOperation:
            print('Write numbers, please!\n')
    while True:
        print('------------------\n'
              '1) Sum\n'
              '2) Difference\n'
              '3) Multiplication\n'
              '4) Division\n'
              '5) Change numbers\n'
              '6) Exit\n')
        ch = 0
        try:
            ch = int(input('Make a choice: '))
            if ch > 6:
                raise ChoiceException()
        except ChoiceException:
            print(ChoiceException('Wrong choice!\n'))
            break
        if ch == 1:
            print(f'Sum: {math_obj.add}')
        elif ch == 2:
            print(f'Difference: {math_obj.sub}')
        elif ch == 3:
            print(f'Multiplication: {math_obj.mul}')
        elif ch == 4:
            try:
                print(f'Division: {math_obj.truediv}')
            except ZeroDivisionError:
                print('Division by zero! Change second number, please!\n')
                break
        elif ch == 5:
            while True:
                try:
                    num1 = Decimal(input('Input firs number: '))
                    num2 = Decimal(input('Input second number: '))
                    math_obj.num1 = num1
                    math_obj.num2 = num2
                    break
                except NameError:
                    print('Write numbers, please!\n')
                except InvalidOperation:
                    print('Write numbers, please!\n')
        else:
            break
    if input('Do you want to continue?\nEnter - continue. N - exit. :') == 'N':
        break
