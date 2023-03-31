def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    every_other = []
    every_other_tracker = 0
    for item in lst:
        every_other_tracker += 1
        if every_other_tracker % 2 == 1:
            every_other.append(item)
    return every_other
