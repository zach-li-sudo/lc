# sol 1. brute force
# def twoSum(nums, target):
#     for i in range(0, len(nums)):
#         for j in range(i, len(nums)):
#             if target == (nums[i]+nums[j]):
#                 return [i, j]

#     return None

# sol 2: hash table, record each sol
def twoSum(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hashtable:
            return [i, hashtable[comp]]
        else:
            hashtable[nums[i]] = i




nums = [2,7,11,15]
target = 26
print(twoSum(nums, target))