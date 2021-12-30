def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    ni = nj = nk = float('inf')
    for n in nums:
        if n <= ni:
            ni = n
        elif ni < n and n < nj:
            nj = n
        elif nj < n and n < nk:
            nk = n
    # print(ni, nj, nk)
    if ni < nj and nj < nk and nk < float('inf'):
        return True
    else:
        return False



# nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
# nums = [1,2,1,3]
# nums = [1,2,3,1,2,1]
print(increasingTriplet(nums))