# class Solution:
#     def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
#         ans = []
#         ds = set(to_delete)
        
#         def remove_node(node):
#             if node is None: return None # return none if none
#             node.left = remove_node(node.left)
#             node.right = remove_node(node.right)
#             if node.val not in ds:
#                 return node
#             if node.left:
#                 ans.append(node.left)
#             if node.right:
#                 ans.append(node.right)            
#             return None

#         root = remove_node(root)
#         if root:
#             ans.append(root)
#         return ans


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        db = set(to_delete)
        def remove(node):
            if node is None: return None
            node.left = remove(node.left)
            node.right = remove(node.right)
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            # if node is leaf node
            return None
        
        if root is None:
            return None
        root = remove(root)
        return ans