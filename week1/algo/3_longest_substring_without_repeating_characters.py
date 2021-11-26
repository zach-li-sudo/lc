# sol 1: brute force, o(n^3)

# sol 2: hash map as the sliding window, fast and slow pointers
def lengthOfLongestSubstring(s):
    if len(s) <= 1: return len(s)

    charFound = {}
    i = j = 0
    longest = 0

    for j in range(len(s)):
        singleChar = s[j]
        if singleChar in charFound and i <= charFound[singleChar]:
            i = charFound[singleChar] + 1
        else:
            longest = max(longest, j - i + 1)
        
        charFound[singleChar] = j

    
    return longest


# s = "abcabcbb"
s = "bbbbb"
# s = "pwwkew"
print(lengthOfLongestSubstring(s))