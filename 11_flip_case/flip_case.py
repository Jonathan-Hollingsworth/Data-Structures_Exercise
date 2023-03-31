def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_to_list = []
    for letter in phrase:
        if letter.upper() == to_swap or letter.lower() == to_swap:
            letter = letter.swapcase() 
        phrase_to_list.append(letter)
    return ''.join(phrase_to_list)