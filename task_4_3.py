dict = {
    'test':'test_value',
    'europe':'eur',
    'dollar':'usd',
    'ruble':'rub'
}
for key in list(dict):
    dict[key + str(len(key))] = dict[key]
    del dict[key]
print(dict)
