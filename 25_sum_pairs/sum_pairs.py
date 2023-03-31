def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    checked = []
    answer = []
    nums_length = len(nums)
    index_tracker = range(nums_length)
    for index in index_tracker:
        num1 = nums[index]
        checked.append(num1)
        difference = goal - num1
        for num2 in checked:
            if num2 == difference:
                answer.append(num1)
                answer.append(num2)
                answer.sort(reverse=True)
                return tuple(answer)
    return ()
