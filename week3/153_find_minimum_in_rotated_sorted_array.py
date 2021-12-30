class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        def find_pivot(nums):
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < nums[hi]:
                    hi = mid
                elif nums[lo] < nums[mid]:
                    lo = mid
                elif hi - lo == 1 and nums[lo] > nums[hi]:
                    return [lo, hi]
            return []
        
        pivots = find_pivot(nums)
        if len(pivots) == 0:
            return nums[0]
        else:
            return nums[pivots[1]]


# nums = [4,5,6,7,0,1,2]
# nums = [3,4,5,1,2]

nums = [11, 13, 15, 17]
sol = Solution()
print(sol.findMin(nums))