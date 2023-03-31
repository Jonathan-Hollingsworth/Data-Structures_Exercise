def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    first_letter = phrase[0]
    first_upper = first_letter.upper()
    capitalized = phrase.replace(first_letter, first_upper, 1)
    return capitalized