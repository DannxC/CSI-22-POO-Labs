import random

def filter_even_numbers(lst):
    """
    Returns a new list containing only the even numbers from the input list.
    """
    return list(filter(lambda x: x % 2 == 0, lst))

random_lst = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_lst)
even_lst = filter_even_numbers(random_lst)
print("Filtered list (even numbers only):", even_lst)