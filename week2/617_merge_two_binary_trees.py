class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # recursion
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None or root2 is None:
            return root1 or root2
        
        if root1 is not None and root2 is not None:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2

    # iteration
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None or root2 is None:
            return root1 or root2
        
        queue = collections.deque([(root1, root2)])
        while queue:
            node1, node2 = queue.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if node1.left is None and node2.left is not None:
                    node1.left = TreeNode(0)
                if node1.right is None and node2.right is not None:
                    node1.right = TreeNode(0)
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        
        return root1

    # my solve, not AC, check tomorrow
    def mergeTrees(root1, root2):
        if root1 is None or root2 is None:
            return root1 and root2
        
        queue = deque([(root1, root2)])
        root = TreeNode(0)
        root.val = root1.val + root2.val
        root.left, root.right = None, None
        queue_root = deque([root])

        while queue:
            node1, node2 = queue.pop()
            current_node = queue_root.pop()
            if node1 is not None and node2 is not None:
                current_node.val = node1.val + node2.val
            elif node1 is None and node2 is None:
                current_node = None
            else:
                queue.appendleft((node1.left, node2.left))
                queue.appendleft((node1.right, node2.right))
                queue_root.appendleft(TreeNode(0))

        return root