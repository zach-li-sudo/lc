class Solution:
    # sol 1. kind of cheat :)
    # def search(self, nums, target):
    #     try:
    #         idx = nums.index(target)
    #         return idx
    #     except:
    #         return -1

    # # sol 2. binary search
    # def search(self, nums, target):
    #     if nums is None:
    #         return -1
    #     # find pivot
    #     def find_pivot(nums):
    #         lo = 0
    #         hi = len(nums) - 1
    #         while lo < hi:
    #             mid = lo + (hi - lo) // 2
    #             if nums[mid] < 


        # split into two part
        # find target in one of the part           
        



nums = [4,5,6,7,0,1,2]
target = 5
sol = Solution()
print(sol.search(nums, target))
