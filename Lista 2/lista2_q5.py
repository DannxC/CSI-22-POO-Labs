def matrix_multiply(A, B):
    """
    Multiplies two matrices and returns the result.
    """

    m = len(A)
    n = len(B[0])

    assert len(A[0]) == len(B), "Matrices aren't compatible for multiplication"
    
    # Init the result matrix
    C = [[0] * n for _ in range(m)]

    # Multiply
    for i in range(m):
        for j in range(n):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


# # TEST 1
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# expected = [[19, 22], [43, 50]]
# result = matrix_multiply(A, B)
# assert result == expected, f"Test case 1 failed. Expected {expected}, but got {result}."

# # TEST 2
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[7, 8], [9, 10], [11, 12]]
# expected = [[58, 64], [139, 154]]
# result = matrix_multiply(A, B)
# assert result == expected, f"Test case 2 failed. Expected {expected}, but got {result}."

# # TEST 3
# A = [[1, 2], [3, 4]]
# B = [[5, 6, 7], [8, 9, 10]]
# try:
#     matrix_multiply(A, B)
#     assert False, "Test case 3 failed. Expected AssertionError, but no exception was raised."
# except AssertionError:
#     pass

# print("All tests pass")