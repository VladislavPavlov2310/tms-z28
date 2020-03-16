def reverse_decorator(function):
    def reverse(*args):
        print(args)
        return args[::-1]
    return reverse


@reverse_decorator
def arguments_to_reverse(*args):
    return args


print(arguments_to_reverse(['Hello', 'goodbye'], 23, 10, 2000, 'tms-z28', 2.666, None))
