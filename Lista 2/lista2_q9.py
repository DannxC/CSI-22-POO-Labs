def apply_func_to_rows(matrix, func):
    """
    Applies a function to each row of a matrix and returns a list of the results.
    """
    return list(map(func, matrix))


# TEST

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

results = apply_func_to_rows(matrix, lambda lst: sum(lst))
print(results)