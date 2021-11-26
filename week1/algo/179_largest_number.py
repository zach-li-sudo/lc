# sol 1.
# int->str, split str, str->int; sort; return joined str(int)
# o(n)

# def largestNumber(nums):
#     num_str = []
#     for n in nums:
#         num_str.append(str(n))
    
#     digits = [int(ch) for ch in num_str] 
#     digits.sort(reverse=True)
    
#     return num_str


def largestNumber(num):
    # str_nums = [str(n) for n in nums]
    # # str_nums.sort(cmp=myComparator)
    
    # str_nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
    # return ''.join(num).lstrip('0') or '0'
    num = [str(x) for x in num]
    num.sort(cmp=lambda x, y: cmp(y+x, x+y))
    return ''.join(num).lstrip('0') or '0'




nums = [3,30,34,5,9]
print(largestNumber(nums))
      