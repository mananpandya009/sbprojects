def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    if len(keys) == len(values):
        diction_ary = dict(zip(keys, values))
        print(diction_ary)
        return diction_ary
    elif len(keys) < len(values):
        new_values = values[0:len(keys)]
        diction_ary = dict(zip(keys, new_values))
    elif len(keys) > len(values):
        new_keys = keys[0:len(values)]
        diction_ary = dict(zip(new_keys, values))

    print(diction_ary)
    return diction_ary


two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
