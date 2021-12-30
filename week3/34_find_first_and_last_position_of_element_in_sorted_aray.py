class Solution:
    # sol 1. two pointers, tc o(n)
    # def searchRange(self, nums, target):
    #     if nums is None:
    #         return [-1, -1]
        
    #     if len(nums) == 1:
    #         return [0,0] if target in nums else [-1,-1]

    #     lo = 0
    #     hi = len(nums) - 1

    #     while lo <= hi:
    #         if nums[lo] < target:
    #             lo += 1
    #         elif nums[hi] > target:
    #             hi -= 1
    #         else:
    #             if nums[lo] == target and nums[hi] != target:
    #                 hi -= 1
    #             elif nums[hi] == target and nums[lo] != target:
    #                 lo += 1
    #             elif nums[lo] == target and nums[hi] == target:
    #                 return [lo, hi]
    #     return [-1,-1]

    # sol 2, binary search, tc o(nlogn)
    # def searchRange(self, nums, target):
    #     if nums is None:
    #         return [-1, -1]
    #     if len(nums) == 1:
    #         return [0,0] if target in nums else [-1,-1]
    #     if target not in nums:
    #         return [-1, -1]
        
    #     def binary_search(nums, target):
    #         lo = 0
    #         hi = len(nums) - 1
    #         while lo + 1 < hi:
    #             mid = (lo + hi) // 2 
    #             if nums[mid] < target:
    #                 lo = mid
    #             elif nums[mid] > target:
    #                 hi = mid
    #             else:
    #                 return mid
    #             # print('in loop')
    #         return None

    #     def expand_interval(nums, i):
    #         if i is None:
    #             return [-1, -1]
    #         target = nums[i]
    #         left = right = i
    #         try:
    #             while nums[left-1] == target and left - 1 >= 0:
    #                 left -= 1
    #         except:
    #             pass

    #         try:
    #             while nums[right+1] == target and right + 1 < len(nums):
    #                 right += 1
    #         except:
    #             pass
            
    #         return [left, right]
        
    #     i = binary_search(nums, target)
    #     print(i)
    #     return expand_interval(nums, i)

# nums = [5,7,7,8,8,10]
# target = 8

# nums = [2,2]
# target = 2

nums = [1,2,3]
target = 2

sol = Solution()
print(sol.searchRange(nums, target))