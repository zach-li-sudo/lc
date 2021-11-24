# sol 1: nested iteration, o(n^2), rejected

# sol 2: sort, then linear search, ACCEPTED
# def containsDuplicate(nums):
#     if len(nums) <= 1:
#         return False
#     nums.sort()
#     for i in range(len(nums)-1):
#         if nums[i] == nums[i+1]:
#             return True
#     return False

# sol 3: hashtable, o(n)
# def containsDuplicate(nums):
#     numSet = set()
#     for i in nums:
#         if i in numSet:
#             return True
#         else:
#             numSet.add(i)
#     return False

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



nums = [1,2,3,1]
print(containsDuplicate(nums))