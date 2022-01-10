def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    word_in_letters = list(word.lower())
    count = word_in_letters.count(letter)
    print(count)
    return count


single_letter_count('Hello World', 'h')

single_letter_count("Hello World", 'z')

single_letter_count("Hello World", 'l')