def dict_unpacking(**kwargs):
    return kwargs


result_dict = lambda original_dict: {
    key + key: value
    for key, value in original_dict.items()
}
print(result_dict(dict_unpacking(a=1, b=2, c=3, d=4, e=5)))
