def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    frequency1 = {}
    frequency2 = {}
    iterable_num1 = str(num1)
    iterable_num2 = str(num2)
    num_list1 = list(iterable_num1)
    num_list2 = list(iterable_num2)
    for num in num_list1:
        if frequency1.get(num, 0):
            None
        else:
            frequency1[num] = num_list1.count(num)
    for num in num_list2:
        if frequency2.get(num, 0):
            None
        else:
            frequency2[num] = num_list2.count(num)
    return frequency1 == frequency2