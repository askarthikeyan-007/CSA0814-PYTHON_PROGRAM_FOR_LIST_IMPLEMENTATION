from itertools import combinations
def generate_combinations(input_list):
    return list(combinations(input_list, len(input_list)))
input_list = [1, 2, 3]
print(generate_combinations(input_list))
