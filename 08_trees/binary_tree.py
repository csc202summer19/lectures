# from linked_stack import *
from linked_queue import *


# NOTE: We expect the user to create trees but not nodes.
class BinaryTree:
    """ A tree in which every node has most two children """

    def __init__(self):
        # The root of the tree:
        self.root = None
        # The number of nodes in the tree:
        self.size = 0


# NOTE: This is a recursive data structure!
class Node:
    """ A node in a binary tree """

    def __init__(self, value, left, right):
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


tree = BinaryTree()
tree.size = 8
tree.root =\
    Node(5,
         Node(11,
              Node(22, None, None),
              Node(3,
                   Node(14, None, None),
                   Node(43, None, None))),
         Node(-2,
              Node(60, None, None),
              None))


# Recursive pre-order traversal:
# def print_preorder(node):
#     """ Print all the nodes in a tree with a pre-order traversal. """
#     if node is None:
#         # If you want to do something with an empty tree, do it here.
#         pass
#     else:
#         # Self:
#         print("    %s" % node.value)
#         # Left:
#         print_preorder(node.left)
#         # Right:
#         print_preorder(node.right)


# Iterative pre-order traversal:
# def print_preorder(root):
#     # Create a "stack of jobs".
#     stack = Stack()
#     push(stack, root)
# 
#     # While there are still more jobs to be done.
#     while size(stack) > 0:
#         # Get the next job.
#         node = pop(stack)
# 
#         # Self:
#         print("    %s" % node.value)
# 
#         # NOTE: A stack is a LIFO structure; if we want to print the left
#         #       first, then we have to push it last.
#         # Right:
#         if node.right is not None:
#             push(stack, node.right)
#         # Left:
#         if node.left is not None:
#             push(stack, node.left)


# Level-order traversal:
def print_levelorder(root):
    # Create a "queue of jobs".
    queue = Queue()
    enqueue(queue, root)

    # While there are still more jobs to be done.
    while size(queue) > 0:
        # Get the next job.
        node = dequeue(queue)

        # Self:
        print("    %s" % node.value)

        # Left:
        if node.left is not None:
            enqueue(queue, node.left)
        # Right:
        if node.right is not None:
            enqueue(queue, node.right)


print_levelorder(tree.root)
