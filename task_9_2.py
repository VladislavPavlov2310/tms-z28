def dict_unpacking(**kwargs):
    return kwargs

# def keys(key):
#     return key + key


result_dict = {
    (lambda key: key + key): value
    for key, value in dict_unpacking(a=1, b=2, c=3).items()
}
print(result_dict)
