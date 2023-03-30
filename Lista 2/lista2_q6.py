def reverse_list(lst):
    """
    Returns a generator that yields the items of the input list in reverse order.
    """
    for item in reversed(lst):
        yield item

lst = [4, 7, 8]
gen = reverse_list(lst)
print(next(gen))
print(next(gen))
print(next(gen))