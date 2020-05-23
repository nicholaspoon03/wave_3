dictionary = {"one": 1, "two": 2, "three": 3, "four": 4}
ages = {"Nicholas": 17, "Jerry": 16, "Conrad": 10, "Leo": 17, "Katherine": 17}
month_of_birth = {"Nicholas": "January", "Jerry": "July", "Conrad": "November", "Dennis": "November"}

def reverse_lookup(dictionary, value):
    corresponding_keys = []
    for i, j in dictionary.items():
        if value == j:
            corresponding_keys.append(i)
    
    if len(corresponding_keys) == 0:
        return "No corresponding keys"
    else:
        return corresponding_keys


print(f'{reverse_lookup(dictionary, 1)} corresponds to 1.')
print(f'{reverse_lookup(ages, 17)} are 17.')
print(f'{reverse_lookup(month_of_birth, "November")} are born in November.')
print(f'{reverse_lookup(month_of_birth, "March")} for March')