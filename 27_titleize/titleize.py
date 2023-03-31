def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lower_phrase = phrase.lower()
    separate_words = lower_phrase.split(' ')
    for word in separate_words:
        word_index  = separate_words.index(word)
        capitalized = word.capitalize()
        separate_words.insert(word_index, capitalized)
        separate_words.pop(word_index + 1)

    titleized = ' '.join(separate_words)
    return titleized