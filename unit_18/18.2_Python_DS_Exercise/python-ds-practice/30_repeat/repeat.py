def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if type(num) == int:
        str = phrase * num
        print(str)
        return str
    else:
        return None


repeat('*', 3)
repeat('abc', 2)
repeat('abc', 0)
repeat('abc', -1)
repeat('abc', 'nope')