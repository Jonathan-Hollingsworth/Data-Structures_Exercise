def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    greater_count = 0
    if nums:
        for num1 in nums:
            idx1 = nums.index(num1)
            for num2 in nums:
                idx2 = nums.index(num2)
                if num2 > num1 and idx2 > idx1:
                    greater_count += 1
    return greater_count