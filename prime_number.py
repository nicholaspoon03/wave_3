number = int(input('Enter an integer: '))


def prime_number(number):
    prime = False
    if number == 1:
        pass
    elif number == 2:
        prime = True
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
            else:
                prime = True
    return prime


if prime_number(number):
    print('Prime')
else:
    print('Not Prime')