def check_chars(str1, str2):
    """
    Check if all characters in str1 are present in str2.
    """
    for c in str1:
        if c not in str2:
            return False
    return True


# TEST

# string1 = "hello"
# string2 = "world, hell"
# result = check_chars(string1, string2)
# if result:
#     print("All characters of", string1, "are present in", string2)
# else:
#     print("Not all characters of", string1, "are present in", string2)