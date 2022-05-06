def add_tuple_lists(list_a, list_b):
    """ Add together two lists of tuples of integers.

    Keyword arguments:
    list_a -- a list of tuples of integers, all of which have the same length
    list_b -- another list of tuples of integers, which have the same length as list_a

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in list a and list b
    """
    result = []
    for i in range(len(list_a)):
        sum_tup = []
        for j in range(len(list_a[0])):
            sum_tup.append(list_a[i][j] + list_b[i][j])
        result.append(tuple(sum_tup))
    return result
