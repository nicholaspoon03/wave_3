n = int(input('Enter an integer (2 or greater): '))
number = n
factor = 2
factor_list = []
prime = False

if n >= 2:
    for i in range(2, n):
        if n == 2:
            prime = True
            break
        elif n % i == 0:
            prime = False
            break
        else:
            prime = True
    
    if prime:
        factor_list.append(n)
    else:
        while factor <= n:
            if number % factor == 0:
                factor_list.append(factor)
                number /= factor
                factor = 2
            else:
                factor += 1

    print(f'The prime factors of {n} are:')
    for i in factor_list:
        print(i)
else:
    print('Please enter a valid number.')
