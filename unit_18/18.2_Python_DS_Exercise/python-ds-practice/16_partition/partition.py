def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    l1 = []
    l2 = []
    master = []
    for item in lst:
        if fn(item):
            l1.append(item)
        else:
            l2.append(item)
    master.append(l1)
    master.append(l2)

    print(master)
    return master


def is_even(num):
    if num % 2 == 0:
        return num
    else:
        return None


def is_string(el):
    if isinstance(el, str):
        return el
    else:
        return None


partition([1, 2, 3, 4], is_even)
partition(["hi", None, 6, "bye"], is_string)
