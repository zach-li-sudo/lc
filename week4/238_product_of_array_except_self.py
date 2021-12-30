def productExceptSelf(nums):
    product = 1
    num_of_zeros = 0
    for n in nums:
        if n == 0:
            num_of_zeros += 1
        else:
            product *= n
    
    results = len(nums) * [0]
    if num_of_zeros >= 2:
        return results
    elif num_of_zeros == 1:
        for i in range(len(nums)):
            if nums[i] == 0:
                results[i] = product
            else:
                results[i] = 0
    else:
        for i in range(len(nums)):
            results[i] = int(product / nums[i])
    
    return results
    


# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))