from itertools import permutations


def permute(nums):

    return [list(p) for p in permutations(nums)]


nums = [1,2,3]
print(permute(nums))
