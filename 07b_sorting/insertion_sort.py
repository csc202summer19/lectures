def insertion_sort(lst):
    """ Sort a list. """

    # NOTE: The first element, by itself, is already sorted.
    for current in range(1, len(lst)):
        value = lst[current]
        previous = current - 1

        # Until we find something smaller or the beginning of the list.
        while previous >= 0 and value < lst[previous]:
            lst[previous + 1] = lst[previous]
            previous -= 1

        # We have now found the index of the element *before* value.
        lst[previous + 1] = value

    return lst
