class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     # find node
    #     # return node subtree
    #     if root is None:
    #         return None
        
    #     stack = collections.deque([root, ])

    #     while stack:
    #         node = stack.popleft()
    #         if node.val == val:
    #             return node
    #         elif val < node.val and node.left is not None:
    #             stack.append(node.left)
    #             continue
    #         elif node.right is not None:
    #             stack.append(node.right)
    #             continue
    #         return None
    #     return Nones

    # recursive
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

        return None