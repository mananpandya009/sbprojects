def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        print(f'{a} is greater than {b}')
    elif a == b:
        print(f'{a} is equal to {b}')
    else:
        print(f'{b} is greater than {a}')


number_compare(2, 6)

number_compare(-1, 0)

number_compare(9,9)
