elem = int(input('Two first elements are: '))
fib_list = [elem, elem]
for i in range(13):
    fib_list.append(fib_list[-1] + fib_list[-2])
print(fib_list)