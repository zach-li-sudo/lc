class Solution:
    # def singleNumber(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     seen = {}
    #     for n in nums:
    #         if n not in seen:
    #             seen.update({n: 1})
    #         else:
    #             seen.update({n: 2})
        
    #     for key, value in seen.items():
    #         if value == 1:
    #             return key

    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)
        
        return list(seen)[0]


# nums = [2,2,1]
nums = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber(nums))