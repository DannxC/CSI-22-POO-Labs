def tuple_averages(tup):
    """
    Computes the average of each tuple within a tuple of tuples and returns a tuple of these averages.
    """
    n = len(tup)
    avg_tup = []
    for i in range(n):
        m = len(tup[i])
        avg = sum(tup[i]) / m
        avg_tup.append(avg)
    return tuple(avg_tup)

# TEST

# tup = [(2, 3, 4), (3, 4, 5, 6), (2, 4), (4, 8, 9)]
# avg_tup = tuple_averages(tup)
# print(avg_tup)