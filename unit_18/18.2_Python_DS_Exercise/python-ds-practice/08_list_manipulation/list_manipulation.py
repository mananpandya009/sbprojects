def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    list = lst
    command = command
    location = location
    value = value

    if command == 'remove':
        if location == 'beginning':
            return list.pop(0)
        elif location == 'end':
            return list.pop(-1)
        else:
            return None
    elif command == 'add':
        if location == 'beginning':
            return list.insert(0, value)
        elif location == 'end':
            return list.append(value)
        else:
            return None

    else:
        return None


lst = [1, 2, 3,4,5,6,7,8,9]
print(list_manipulation(lst, 'remove', 'end'))
print(list_manipulation(lst, 'remove', 'beginning'))
print(list_manipulation(lst, 'remove', 'end'))
print(list_manipulation(lst, 'remove', 'beginning'))
print(list_manipulation(lst, 'add', 'beginning', 20))
print(list_manipulation(lst, 'add', 'end', 30))
print(list_manipulation(lst, 'foo', 'end'))
print(list_manipulation(lst, 'add', 'dunno'))
print(lst)