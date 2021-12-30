class Solution:
    # sol 1: hash table: tc o(n), sc o(n)
    # def majorityElement(self, nums):
    #     hp = dict()
    #     for n in nums:
    #         if n not in hp:
    #             hp.update({n: 1})
    #         else:
    #             hp[n] += 1
        
    #     for key, value in hp.items():
    #         if value > (len(nums) // 2):
    #             return key
    #     return None

    # sol 2: sort in place:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2 + 1]



nums = [3,2,3]
# nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))
