def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    lst = list(phrase)
    lst[0:1] = lst[0].upper()
    new_str = ''.join(lst)

    print(new_str)


capitalize('python')
capitalize('only first word')