def sortedSquares(nums):
    squares = len(nums) * [0]

    l = 0
    r = len(nums) - 1

    for i in range(len(squares)-1, -1, -1):
        if nums[l]**2 >= nums[r]**2:
            squares[i] = nums[l]**2
            l += 1
        else:
            squares[i] = nums[r]**2
            r -= 1
    
    return squares

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
    