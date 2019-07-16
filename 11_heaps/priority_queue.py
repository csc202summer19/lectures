class PriorityQueue:
    """ A collection of elements with priority """

    def __init__(self, capacity = 16):
        # The array to store the backing binary heap:
        self.heap = [None] * (capacity + 1)
        # The length of the array, less one:
        self.capacity = capacity
        # The number of elements in this priority queue:
        self.size = 0


def enqueue(pqueue, value):
    """ Add a value to a priority queue """
    # If there is no more capacity, then:
    #     Double the backing heap's array.
    # Add the value as the next leaf (current index = size + 1)
    # While a parent (current index // 2) exists and is larger, do:
    #     Swap the current value with its parent.
    #     Set the current index equal to the parent index.
    # Increment the size
    pass


def dequeue(pqueue):
    """ Remove the highest priority element from a priority queue """
    # Save the root (current index = 1) in a temporary variable.
    # Put the last leaf (index = size) into the root.
    # While a child (left child = current index * 2,
    #               (right child = current index * 2 + 1) exists, do:
    #     If neither child is larger, then:
    #          Break the loop -- this could be in the loop condition.
    #     Else, if the right child exists and is larger than both the left
    #      child and the current, then:
    #          Swap with the right child.
    #          Set the current index to the right child.
    #     Else (either the right child does not exist or it is smaller than the
    #      left child, and the left is larger than the parent):
    #          Swap with the left child.
    #          Set the current index to the left child.
    # Decrement the size.
    # Return the old root.
    pass
