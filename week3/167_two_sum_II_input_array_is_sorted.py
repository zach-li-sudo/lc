class Solution:
    def twoSum(self, numbers, target):
        lo = 0
        hi = len(numbers) - 1

        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo+1, hi+1]
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            else:
                hi -= 1




numbers = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(numbers, target))