def del_even_decorator(function):
    def del_even(num_list):
        return list(filter(lambda x: (x % 2 != 0), num_list))
    return del_even


@del_even_decorator
def just_return_list(yes_that_list):
    return yes_that_list


main_list = [10, 2, 3, 41, 5, 66, 72, 89, 9, 10]
print(just_return_list(main_list))
