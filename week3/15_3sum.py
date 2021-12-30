from collections import Counter
class Solution:
    # def threeSum(self, nums):
    #     if len(nums) < 3:
    #         return []

    #     # hashtable = set(nums)
    #     results = []
    #     nums.sort()

    #     for i in range(len(nums)-2):
    #         lo = i + 1
    #         hi = len(nums) - 1
    #         pivot = nums[i]
    #         while lo < hi:
    #             if pivot + nums[lo] + nums[hi] == 0:
    #                 if [pivot, nums[lo], nums[hi]] not in results:
    #                     results.append([pivot, nums[lo], nums[hi]])
    #                 hi -= 1
    #                 lo += 1
                    
    #             elif pivot + nums[lo] + nums[hi] < 0:
    #                 lo += 1
    #             else:
    #                 hi -= 1
        
    #     return results
    
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()
        results = []
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            pivot = nums[i]

            while lo < hi:
                sum3 = nums[lo] + nums[hi] + pivot
                result  = [pivot, nums[lo], nums[hi]]
                if sum3 == 0:
                    if result not in results:
                        results.append(result)
                    lo += 1
                elif sum3 < 0:
                    lo += 1
                else:
                    hi -= 1
        
        return results




# nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
sol = Solution()
print(sol.threeSum(nums))