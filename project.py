def add_tuple_lists(list_a, list_b):
    """ Add together two lists of tuples of integers.

    Keyword arguments:
    list_a -- a list of tuples of integers, all of which have the same length
    list_b -- another list of tuples of integers, which have the same length as list_a

    Returns:
    a single list of tuples, each one being the sum of the equivalent tuples in list a and list b
    """

    # two lists of lists
    # both lists have same length
    # each inner tuple has the same length

    # list_a = [(1,)]
    # list_b = [(1,)]
    # result = [(2,)]

    # list_a = [(1, 1)]
    # list_b = [(1, 2)]
    # result = [(2, 3)]

    # list_a = [(1, 1), (1, 1)]
    # list_b = [(1, 2), (2, 1)]
    # result = [(2, 3), (3, 2)]

    # take first tuple from list a
    # take first tuple from list b
    # take first value from first tuple
    # take first value from second tuple
    # sum them
    # add then to a new tuple
    # append to output list
    
    first_tuple_a = list_a[0]
    first_tuple_b = list_b[0]
    first_value_tuple_a = first_tuple_a[0]
    first_value_tuple_b = first_tuple_b[0]
    sum_of_values = first_value_tuple_a + first_value_tuple_b
    new_tuple = tuple(sum_of_values)
    output_list = []
    output_list.append(new_tuple)
    return output_list

    # take first tuple from list a
    # take first tuple from list b
    # take first value from first tuple
    # take first value from second tuple
    # sum them
    # add then to a new tuple
    # take second value from first tuple
    # take second value from second tuple
    # sum them
    # add then to a new tuple
    # append to output list

    first_tuple_a = list_a[0]
    first_tuple_b = list_b[0]

    length_of_tuple = len(first_tuple_a)

    sums = []

    for i in range(length_of_tuple):
        value_tuple_a = first_tuple_a[i]
        value_tuple_b = first_tuple_b[i]
        sum_of_values = value_tuple_a + value_tuple_b
        sums.append(sum_of_values)

    new_tuple = tuple(sums)

    output_list = []
    output_list.append(new_tuple)
    return output_list

    # take first tuple from list a
    # take first tuple from list b
    # take first value from first tuple
    # take first value from second tuple
    # sum them
    # add then to a new tuple
    # take second value from first tuple
    # take second value from second tuple
    # sum them
    # add then to a new tuple
    # append to output list
    # take second tuple from list a
    # take second tuple from list b
    # take first value from first tuple
    # take first value from second tuple
    # sum them
    # add then to a new tuple
    # take second value from first tuple
    # take second value from second tuple
    # sum them
    # add then to a new tuple
    # append to output list

