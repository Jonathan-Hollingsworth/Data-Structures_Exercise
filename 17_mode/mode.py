def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    old_count = 0
    most_common = 0
    for num in nums:
        new_count = nums.count(num)
        if new_count > old_count:
            most_common = num
    return most_common