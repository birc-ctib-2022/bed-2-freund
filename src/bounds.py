"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""

def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """

    if x[-1] < v:
        return len(x)

    low, high = 0, len(x) - 1
    found = None
    while low <= high:
        mid = (low + high) // 2
        if x[mid] == v:
            found, high = mid, mid - 1
        elif x[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    if found == None:
        return len(x)
    return found


def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """

    if x[-1] < v:
        return len(x)

    low, high = 0, len(x) - 1
    found = None
    while low <= high:
        mid = (low + high) // 2
        if x[mid] == v:
            found, low = mid, mid + 1
        elif x[mid] < v:
            low = mid + 1
        else:
            high = mid - 1

    if found == None:
        return len(x)
    return found
