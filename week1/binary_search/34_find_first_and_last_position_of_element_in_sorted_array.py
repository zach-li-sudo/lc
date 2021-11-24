def searchRange(nums: List[int], target: int) -> List[int]:
    left, right = bsLeft(nums, target), bsRight(nums, target)



def bsLeft(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:







nums = [5,7,7,8,8,10]
target = 6

print(searchRange(nums, target))


# convert to a set