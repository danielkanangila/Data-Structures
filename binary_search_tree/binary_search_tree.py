"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # if the root value is less than the target
        # check to right of tree
        if self.value < target:
            if self.right is None:
                return False
            return self.right.contains(target)
        # if the root value is greater than the target
        # check to the left of the true
        else:
            if self.left is None:
                return False
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Initialize max value
        max_value = self.value

        while self.right:
            max_value = max(max_value, self.right.value)
            self = self.right

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # fn == callback function
        fn(self.value)
        # check is left or right is not none
        # then call for_each and pass the callback to the next node. `recursive`
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for node
        # add the firs node to the queue
        # while queue is not empty
        #  remove the first from the queue
        # print the removed node
        # add all children into the queue
        q = Queue()
        q.enqueue(node)
        while len(q) > 0:
            top_node = q.dequeue()
            print(top_node.value)
            if top_node.left:
                q.enqueue(top_node.left)
            if top_node.right:
                q.enqueue(top_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a stack for node
        # add the node to the stack
        # while teh stack is not empty
        # get the current node from the top of the stack
        # print that node
        # add all children to the stack
        # remember, the oreder you add the children, will matter
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
