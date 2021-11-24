# # sol 1. brute force, rejected, time limit exceeded
# def maxSubArray(nums):
#     max_array = -inf
#     for i in range(len(nums)):
#         new_subarray = 0
#         for j in range(i, len(nums)):
#             new_subarray += nums[j]
#             max_array = max(max_array, new_subarray)
    
#     return max_array


# sol 2: dp Cadane's algorithm
def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
    return max(nums)