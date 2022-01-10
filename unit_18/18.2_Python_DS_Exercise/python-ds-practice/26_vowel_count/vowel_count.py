def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    letter_dict = dict()
    for letter in list(phrase.lower()):
        if not letter_dict.get(letter) and letter in 'aeiou':
            letter_dict[letter] = list(phrase).count(letter)


    print(letter_dict)
    return letter_dict


vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!')