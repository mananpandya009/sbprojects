def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    forward_str_list = list(phrase)
    reverse_str = ''.join(forward_str_list[::-1])

    if reverse_str == phrase:
        print(f'{reverse_str} is a palindrome')
        return True
    else:
        print(f'{reverse_str} is not a palindrome')
        return False


is_palindrome('tacocat')
is_palindrome('robert')
