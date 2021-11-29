# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # dfs, recursion
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        output = []
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) + 1
    
    # iteration, stack
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth