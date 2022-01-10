def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    forward_str_list = list(phrase)
    reverse_str = ''.join(forward_str_list[::-1])

    print(reverse_str);
    return reverse_str


reverse_string("hello")
