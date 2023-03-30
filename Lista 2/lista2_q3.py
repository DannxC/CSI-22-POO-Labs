def alnum_strings(lst):
    """
    This function filters a list of strings and returns only those that contain alphanumeric characters.
    """
    result = []
    for str in lst:
        if any(c.isalnum() for c in str):
            result.append(str)
    return result

# TEST

lst = ['123', 'abc', 'abc123', '!@#$%^&*()', 'def_456', 'ghi 789', '^']
result = alnum_strings(lst)
print(result)
