class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursion
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if root is None:
    #         return False

    #     targetSum -= root.val
    #     if root.left is None and root.right is None:
    #         return sum == 0
    #     return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    # iteration
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, targetSum - root.val), ]
        while stack:
            node, current_sum = stack.pop()
            if node.left is None and node.right is None and current_sum == 0: # reach a leaf node
                return True
            if node.right:
                stack.append((node.right, current_sum - node.right.val))
            if node.left:
                stack.append((node.left, current_sum - node.left.val))
        
        return False