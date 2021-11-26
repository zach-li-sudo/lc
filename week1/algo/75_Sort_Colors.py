# from collections import Counter
# def sortColors(nums):
#     c = Counter(nums)
#     sorted_list = []
#     for i in range(3):
#         for j in range(c[i]):
#             sorted_list.append(i)
#     nums = sorted_list[:]
    

def sortColors(nums):
    lb0 = 0
    ub2 = len(nums) - 1
    curr = 0
    
    while lb0 < ub2:
        if nums[curr] == 2:
            pass

nums = [2,0,2,1,1,0]
print(sortColors(nums))