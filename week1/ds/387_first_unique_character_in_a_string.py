# sol 1. hash table
def firstUniqChar(s):
    if not s: return -1
    if len(s) == 1: return 0

    charFound = {}
    for ch in s:
        if ch not in charFound:
            charFound[ch] = 1
        else:
            charFound[ch] += 1
    
    for i in range(len(s)):
        ch = s[i]
        if charFound[ch] == 1:
            return i
    
    return -1



s = "loveleetcode"
print(firstUniqChar(s))