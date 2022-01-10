def print_upper_words(word_list,must_start_with):
    for word in word_list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
        
        


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
