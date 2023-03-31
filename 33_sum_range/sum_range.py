def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0
    nums_length = len(nums)
    if not end or end > nums_length - 1:
        indices = range(start, nums_length)
        for index in indices:
            sum += nums[index]
    else:
        indices = range(start, end + 1)
        for index in indices:
            sum += nums[index]
    return sum
