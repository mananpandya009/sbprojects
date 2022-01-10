def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = (phrase.lower()).split()
    new_phrase_list = []
    for word in phrase_list:
        lst = list(word)
        lst[0:1] = lst[0].upper()

        new_str = ''.join(lst)
        new_phrase_list.append(new_str)

    new_phrase = ' '.join(new_phrase_list)

    print(new_phrase)



titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')