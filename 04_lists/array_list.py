class List:
    """ Implement the List ADT using arrays. """

    def __init__(self):
        # The backing array:
        self.array = [None] * 4
        # The length of the backing array:
        self.capacity = 4
        # The number of elements in the list:
        self.size = 0


def add(lst, idx, value):
    """ Add an element to a list at an index. """
    # If there is not enough capacity, then:
    #     Create a new array with twice the capacity.
    #     Copy over every value in the old array.
    #     Replace "lst.array" with the new array.
    #     Update "lst.capacity".
    # Shift everything from "idx" to "lst.size - 1" right by 1.
    # Set "lst.array[idx] = value".
    # Increment the size.
    pass


def set(lst, idx, value):
    """ Set the value at an index. """
    # Set "lst.array[idx] = value".
    pass


def remove(lst, idx):
    """ Remove the value at an index. """
    # Shift everything from "idx + 1" to "lst.size - 1" left by 1.
    # Decrement the size.
    pass
