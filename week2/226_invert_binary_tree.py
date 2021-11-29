class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import queue
class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # bfs recursion
    #     if root is None:
    #         return root

    #     right = self.invertTree(root.right)
    #     left = self.invertTree(root.left)
    #     root.left = right
    #     root.right = left
    #     return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iteration, bfs
        if root is None:
            return root
        
        queue = deque([root,])
        while queue:
            current_node = queue.pop()
            current_node.left, current_node.right = current_node.right, current_node.left
            if current_node.left is not None: queue.append(current_node.left)
            if current_node.right is not None: queue.append(current_node.right)
        
        return root
