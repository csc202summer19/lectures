class Stack:
    """ A last-in, first-out collection of elements """

    def __init__(self):
        # The backing array:
        self.array = [None] * 4
        # The length of the backing array:
        self.capacity = 4
        # The number of elements in the stack:
        # NOTE: The top-of-stack is always "size - 1".
        self.size = 0


def push(stack, value):
    # NOTE: Since the TOS is "size - 1", the next available spot must be
    #       "size" itself.
    # Double the capacity if necessary.
    # Set "stack.array[stack.size] = value".
    # Increment the size.
    pass


def pop(stack):
    # Decrement the size.
    # Return the element at "stack.array[stack.size]".
    pass


def peek(stack):
    # Return the element at "stack.array[stack.size - 1]".
    pass
