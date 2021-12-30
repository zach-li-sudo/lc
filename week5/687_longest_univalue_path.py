# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
        
    def univaluePath(self, node):
            if node is None: return 0
            l = self.univaluePath(node.left)
            r = self.univaluePath(node.right)
            pl = 0
            pr = 0
            if node.left and node.val == node.left.val: 
                pl = l + 1
            if node.right and node.val == node.right.val: 
                pr = r + 1
            self.ans = max(self.ans, pl + pr)
            return max(pl, pr)
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        self.univaluePath(root)
        return self.ans


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def univaluePath(node):
            if node is None: return 0
            l = univaluePath(node.left)
            r = univaluePath(node.right)
            pl = 0
            pr = 0
            if node.left and node.val == node.left.val: pl = l + 1
            if node.right and node.right == node.right.val: pr = r + 1
            self.ans = max(self.ans, pl + pr)
            return max(pl, pr)
        
        univaluePath(root)
        return self.ans