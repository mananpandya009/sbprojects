def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1 = list(str(num1))
    list2 = list(str(num2))
    dict1 = dict()
    dict2 = dict()
    freq_flag = True

    for num in set(list1):
        dict1[num] = list1.count(num)

    for num in set(list2):
        dict2[num] = list2.count(num)
    if len(dict1) == len(dict2):
        for key in dict1.keys():
            if dict1[key] == dict2[key]:
                continue
            else:
                freq_flag = False
                break
    else:
        freq_flag = False

    print(freq_flag)
    return freq_flag


same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)