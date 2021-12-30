# def longestPalindrome(s):
#     if s == "":
#         return 0
#     def check_palindrome(ss):
#         reversed_str = ss[::-1]
#         return reversed_str == ss

#     for length in range(len(s), 0, -1):
#         for i in range(0, len(s)-length+1):
#             substring = s[i:i+length]
#             if check_palindrome(substring):
#                 return substring
#     return 1


def longestPalindrome(s):
    pass

s = "babad"
print(longestPalindrome(s))

