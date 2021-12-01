class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nvals = self.in_order(root)
        nums = [n.val for n in nvals]
        return self.two_sum(nums, k)

    def two_sum(self, nums, k):
        # two pointers
        if len(nums) == 0: return False
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == k:
                return True
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1

        return False

    def in_order(self, root):
        res = []
        if root:
            res += self.in_order(root.left)
            res.append(root)
            res += self.in_order(root.right)
        return res
        