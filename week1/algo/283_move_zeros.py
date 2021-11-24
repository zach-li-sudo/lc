# tc: o(n), cc: o(1)

def moveZeroes(nums):
    if len(nums) != 1:
        
        num_zero = 0
        i = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                num_zero += 1
            else:
                nums[i-num_zero], nums[i] = nums[i], nums[i-num_zero]
                
    return nums

nums = [0, 1]
print(moveZeroes(nums))