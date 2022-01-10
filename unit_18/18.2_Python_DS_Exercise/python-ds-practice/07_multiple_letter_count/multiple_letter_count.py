def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_dict = dict()
    for letter in list(phrase):
        if not letter_dict.get(letter):
            letter_dict[letter] = list(phrase).count(letter)


    print(letter_dict)
    return letter_dict


multiple_letter_count('yay')
multiple_letter_count('Yay')
