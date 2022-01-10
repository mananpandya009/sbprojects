def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    evens = [num for num in nums if num % 2 == 0]
    print(evens)
    number = 1
    if len(evens) > 0:
        for n in evens:
            number *= n
        print(number)
        return number
    else:
        return 1


multiply_even_numbers([2, 3, 4, 5, 6])
multiply_even_numbers([3, 4, 5])
