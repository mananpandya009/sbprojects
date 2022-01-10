def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factor_list = []
    for i in range(num+1):
        if not i == 0:
            if num % i == 0:
                factor_list.append(i)

    print(factor_list)



find_factors(10)
find_factors(11)
find_factors(111)
find_factors(321421)