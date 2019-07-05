def quicksort(lst):
    return _quicksort(lst, 0, len(lst) - 1)


def _quicksort(lst, low, high):
    if low < high:
        # Build the partitions:
        pivot = partition(lst, low, high)
        # Recursively sort them:
        _quicksort(lst, low, pivot - 1)
        _quicksort(lst, pivot + 1, high)
    return lst


def partition(lst, low, high):
    # Arbitrarily choose the first element to be the pivot.
    pivot = low
    left = low + 1
    right = high

    # Keep going until the left passes the right.
    while left <= right:
        # Find an element on the left that's too big.
        while left <= right and lst[left] < lst[pivot]:
            left += 1

        # Find an element on the right that's too small.
        while left <= right and lst[right] > lst[pivot]:
            right -= 1

        # Swap them.
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    # Put the pivot in the right place: we're coming from the left, and we know
    #  the right stops when it finds something smaller.
    lst[pivot], lst[right] = lst[right], lst[pivot]

    # Return the index where we put the pivot so that we know how to recurse on
    #  the partitions.
    return right
