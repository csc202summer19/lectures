class List:
    """ Implements the List ADT using linked nodes."""

    def __init__(self, head = None, size = 0):
        # NOTE: The list will start empty.
        # The head of the backing linked list:
        self.head = head
        # The size of the list:
        self.size = size


class Node:
    """ Encapsulates one value in a linked list."""

    # NOTE: The user never creates nodes.
    # NOTE: This is a recursively-defined data structure: Node is defined in
    #       terms of itself!
    def __init__(self, value, next):
        # The value itself:
        self.value = value
        # A reference to the next Node:
        self.next = next


def add(lst, idx, value):
    """ Add a value at an index. """
    # Create a node containing the value.
    # If we're adding to the beginning:
    #     Set the new node's next to the old head.
    #     Set the head to the new node.
    # Else:
    #     Find the previous node (node with index "idx - 1").
    #     Set the new node's next to the previous node's next.
    #     Set the previous node's next to the new node.
    # Increment the size.
    pass


def remove(lst, idx):
    """ Remove the value at an index. """
    # If we're removing from the beginning:
    #     Set the head to the head's next.
    # Else:
    #     Find the previous node (node with index "idx - 1").
    #     Set the previous node's next to its next node's next.
    # Decrement the size.
    pass
