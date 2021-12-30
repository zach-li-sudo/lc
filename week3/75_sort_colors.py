class Solution:
    # sol 1: hashmap, one pass, tc: o(n), sc: o(1)
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {0:0, 1:0, 2:0}
        for num in nums:
            if num not in hm:
                hm.update({num: 1})
            else:
                hm[num] += 1
        nums[:] = hm[0]*[0] + hm[1]*[1] + hm[2]*[2]
        print(nums)



nums = [2,0,2,1,1,0]
# nums = [0]
sol = Solution()
sol.sortColors(nums)