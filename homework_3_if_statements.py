"""
This file describes work with if statements
"""


def compare_for_equality(a, b, c):
    """
    Checks for equality between any two of arguments.
    If any 2 arguments or all of are equivalent, return True.
    Else - return False.
    """
    a = int(a)
    b = int(b)
    c = int(c)

    if a == b == c:
        return True
    elif a == b:
        return True
    elif b == c:
        return True
    elif c == a:
        return True
    else:
        return False


# Calling the function
print(f'1, 2, 1 = {compare_for_equality(1, 2, 1)}')
print(f'2, 2, 1 = {compare_for_equality(2, 2, 1)}')
print(f'1, 1, 1 = {compare_for_equality(1, 1, 1)}')
print(f'1, 8, 3 = {compare_for_equality(1, 8, 3)}')

print(f'"1", 2, 1 = {compare_for_equality("1", 2, 1)}')
print(f'"3", 3, "3" = {compare_for_equality("3", 3, "3")}')
print(f'"7", "5", "3" = {compare_for_equality("7", "5", "3")}')
