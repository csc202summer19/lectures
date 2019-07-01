class Queue:
    """ A first-in, first-out collection of elements """

    def __init__(self):
        # The backing array:
        self.array = [None] * 4
        # The length of the backing array:
        self.capacity = 4
        # NOTE: In an empty queue, there is no front or back -- we need to
        #       indicate that these indices are invalid.
        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1


def enqueue(queue, value):
    # Double the capacity if necessary, "unwrapping" the queue if it has
    #  wrapped around.
    # If the queue is empty, then:
    #     Put the value at index 0.
    #     Set both front and back to 0.
    # Else, do:
    #     Increment the back.
    #     Wrap the back around to the beginning if necessary.
    #     Put the value at the back.
    pass


def dequeue(queue):
    # Increment the front.
    # Wrap the front around to the beginning if necessary.
    # Return what was at "the old front".
    pass
