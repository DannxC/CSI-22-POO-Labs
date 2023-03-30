def remove_empty_tuples(lst):
    """
    This function takes a list of tuples as input, iterates over the list, and removes 
    any empty tuples found in the list.
    
    OBS: The function modifies the list in place, and does not return anything.
    """
    i = 0
    while i < len(lst):
        if lst[i] == ():
            lst.pop(i)
        else:
            i += 1


# TEST 1

# lst = [(1, 2), (5, ), (), (1, 2, 3), ()]
# remove_empty_tuples(lst)
# print(lst)


# TEST 2

# lst = [(1, 2), (5, ), (), (1, 2, 3), (), (4, 5), (), ()]
# remove_empty_tuples(lst)
# print(lst)