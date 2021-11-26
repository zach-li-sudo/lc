# sol1: find substring of len(s1)
from collections import Counter
def checkInclusion(s1, s2):
    substring_len = len(s1)
    c1 = Counter(s1)

    for i in range(len(s2)-substring_len+1):
        substr = s2[i:i+substring_len]
        #print(substr)
        c2 = Counter(substr)
        if c1 == c2:
            return True

    return False

# s1 = "bca"
# s2 = "abca"

s1 = "ab"
s2 = "eidboaoo"

# s1 = "hello"
# s2 = "ooolleoooleh"

print(checkInclusion(s1, s2))
