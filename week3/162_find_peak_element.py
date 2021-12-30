class Solution:
    def findPeakElement(self, nums):
        if len(nums) <= 2:
            return max(nums)

        lo = 0
        hi = len(nums) - 1
        mid = lo + (hi - lo) // 2
        if mid + 1 < len(nums) and nums[mid] > nums[mid+1] and mid - 1 >= 0 and nums[mid] > nums[mid-1]:
            return mid
        else:
            if self.findPeakElement(nums[lo:mid]) is not None and  self.findPeakElement(nums[mid:hi]) is not None:
                return self.findPeakElement(nums[mid+1:hi])
        return None
        

# nums = [1,2,4,2,5,6]
# nums = [1,2,5]
# nums = [5,3,2,1]

nums = [1,2,3,1]
# [1,2,1,3,5,6,4]


sol = Solution()
print(sol.findPeakElement(nums))