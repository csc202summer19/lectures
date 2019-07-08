class BST:
    """ A binary search tree """

    def __init__(self):
        # The root of the tree:
        self.root = None
        # The number of nodes in the tree:
        self.size = 0


class Node:
    """ A node in a binary search tree """

    def __init__(self, key, left, right):
        # The key contained in this node:
        self.key = key
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def insert(tree, key):
    """ Insert a key into a BST. """
    # If the tree is empty, then:
    #     Create a new node containing the key as the root of the tree.
    # Else:
    #     Call the helper function.
    # Increment the size.
    pass


# NOTE: The node is the recursive structure, not the tree.
def _insert(node, key):
    # If key < the node's key:
    #    If the node does not have a left:
    #        Create a new node containing the key.
    #        Set that new node as the current node's left.
    #    Else:
    #        Recurse left.
    # Else (assuming no duplicates):
    #    If the node does not have a right:
    #        Create a new node containing the key.
    #        Set that new node as the current node's right.
    #    Else:
    #        Recurse right.
    pass


def remove(tree, key):
    # If the tree is empty:
    #     Raise an error.
    # Else:
    #     Call a helper function.
    pass


def _remove(node, key):
    # If the node is None:
    #     Raise an error.
    # Else if the node contains the key:
    #     If the node has no children:
    #         Replace the node with None.
    #     Else if the node has one child:
    #         Replace the node with that child.
    #     Else:
    #         Replace the node with the smallest on the right.
    # Else if key < the node's key:
    #     Recurse left.
    # Else:
    #     Recurse right.
