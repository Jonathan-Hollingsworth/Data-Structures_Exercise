def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    sum1 = 0
    sum2 = 0
    for lst in matrix:
        index = matrix.index(lst)
        sum1 += lst[index]
    matrix.reverse()
    for lst in matrix:
        index = matrix.index(lst)
        sum2 += lst[index]
    return sum1 + sum2