from collections import Counter
def isAnagram(s, t):
    sc = Counter(s)
    rc = Counter(t)
    return sc == rc




s = "anagram"
t = "nagaram"
print(isAnagram(s, t))