# sol 1. o(n)
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

# sol 2. sort + search, o(nlogn) + o(logn)

# nums = [3,2,2,3]
# val = 2
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))