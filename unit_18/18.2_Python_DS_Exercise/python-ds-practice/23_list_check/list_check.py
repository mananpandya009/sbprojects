def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    check_flag = True
    for item in lst:
        if type(item) == list:
            continue
        else:
            check_flag = False
            return False

    return check_flag


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))


