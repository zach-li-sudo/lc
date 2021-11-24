# hash table
def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l, r]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    

    




numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))