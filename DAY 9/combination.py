from itertools import product
a = {
    'key1': ['a', 'b'],
    'key2': ['c', 'd']
}
b =a.values()
combinations = product(*b)
for combo in combinations:
    print(''.join(combo))
