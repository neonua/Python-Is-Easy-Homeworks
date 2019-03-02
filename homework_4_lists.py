"""
This file describes work with lists
"""

# Defining lists
myUniqueList = []
myLeftovers = []


def append(item):
    """
    Appends item to myUniqueList.
    If can't - appends item to myLeftovers.
    """
    print(f'Appending {item} ...')

    # Check if item already in myUniqueList
    if item in myUniqueList:
        # If yes, append value to myLeftovers and return False
        append_to_list(item, myLeftovers, 'Can\'t append to myUniqueList so appending to myLeftovers')
        return False

    # If no, append to myUniqueList and return True
    append_to_list(item, myUniqueList, 'Append to myUniqueList')
    return True


def append_to_list(item, list, text):
    """
    Appends item to list and prints needed info
    """
    print(text)
    list.append(item)
    print_lists()


def print_lists():
    """
    Prints two lists in specific format
    """
    print(f'myUniqueList = {myUniqueList}\nmyLeftovers = {myLeftovers}\n')


# Testing
append(1)
append(1)
append(1)
append('2')
append(2)
append('2')
append([])
append([])
append([1, 2])
append([1, 3])
append([1, 3])
