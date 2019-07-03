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


def merge_sort(lst):
    """ Sort a list in the most beautiful way possible. """
    if len(lst) <= 1:
        return lst
    else:
        return merge(merge_sort(lst[:len(lst) // 2]),
                     merge_sort(lst[len(lst) // 2:]))


def merge(lst_a, lst_b):
    """ Merge two sorted lists together. """
    i = 0
    j = 0
    lst = []

    # Walk down both lists simultaneously.
    while i < len(lst_a) and j < len(lst_b):
        if lst_a[i] < lst_b[j]:
            lst.append(lst_a[i])
            i += 1
        else:
            lst.append(lst_b[j])
            j += 1

    # Take whatever's left and put it into the result.
    # NOTE: *One* of the lists still has unmerged elements.
    lst.extend(lst_a[i:])
    lst.extend(lst_b[j:])

    return lst
