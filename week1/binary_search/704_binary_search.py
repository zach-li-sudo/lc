def search(nums, target):
    l = 0
    r = len(nums) - 1
    mid = (l + r) // 2

    while l <= r:
        if nums[mid] == target:
            return mid
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r) // 2
    return -1 


nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target))