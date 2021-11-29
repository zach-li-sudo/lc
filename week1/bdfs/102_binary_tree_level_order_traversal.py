class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        visited = set()
        queue = []

        if root not in visited:
            queue.append(root.val)
            queue += self.levelOrder(root.left)
            queue += self.levelOrder(root.right)
        
        return queue
