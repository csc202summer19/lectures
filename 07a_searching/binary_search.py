def binary_search(lst, value):
    """ Find an element in a sorted list. """
    
    # Initially, the entire list is unsearched.
    low = 0
    high = len(lst) - 1

    # While there are still elements to be searched.
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    # If we get this far, we couldn't find the element.
    return -1
