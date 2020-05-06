items = int(input('Enter the number of items purchased: '))

def cost(items):
    if items == 0:
        return 0
    elif items == 1:
        return 10.95
    else:
        return round(10.95+2.95*(items-1), 2)

print(f'You purchased {items} items.')
print(f'The shipping charge is ${cost(items)}.')
