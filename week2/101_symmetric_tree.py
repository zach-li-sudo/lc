class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursion
        # if root is None:
        #     return True

        # def is_mirror(node1, node2):
        #     if node1 is None and node2 is None: return True
        #     if node1 is None or node2 is None: return False
        #     return (node1.val == node2.val) and is_mirror(node1.right, node2.left) and is_mirror(node1.left, node2.right)

        # return is_mirror(root.left, root.right)

        # iteration
        if root is None:
            return True
        
        stack = [(root.left, root.right)]

        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None: continue
            if node1 is None or node2 is None: return False
            if node1.val != node2.val: return False # "is not" is not equivalent to "!=" for numbers!

            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        
        return True
