# sol 1. using extra array, 
# time complexity: o(1)
# space complexity: o(n)

# def rotateArray(nums, k):
#     if k == 0:
#         return nums

#     n = len(nums)
#     k = k % n

#     nums1 = nums[:(n-k)]
#     nums2 = nums[(n-k):]
#     nums = nums2 + nums1

#     print(nums)



# sol 2, rotate in-place
def rotateArray(nums, k):
    pass


nums = [1,2,3,4,5,6,7]
k = 3

rotateArray(nums, k)
