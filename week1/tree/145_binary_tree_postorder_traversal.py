class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, traversal_path = [root], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                traversal_path.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return traversal_path


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, traversal_path = [root.left], []

        while stack:
            left = stack.pop()
            if left is not None:
                traversal_path.append(left.val)
                if root.right is not None:
                    stack.append(root.right.val)
                if root is not None:
                    stack.append(root.val)
        return traversal_path
    