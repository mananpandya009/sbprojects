def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_list = []
    for letter in list(phrase):
        if letter == to_swap:
            if letter.islower():
                new_list.append(letter.upper())
            else:
                new_list.append(letter.lower())
        else:
            new_list.append(letter)

    new_string = ''.join(new_list)
    print(new_string)


flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')
