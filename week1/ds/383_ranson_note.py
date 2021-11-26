# sol 1. 2 hast tables, o(2n+m)
# def canConstruct(ransomNote, magazine):
#     def freq_dict(s):
#         freq = {}
#         for ch in s:
#             if ch not in freq:
#                 freq[ch] = 1
#             else:
#                 freq[ch] += 1
#         return freq

#     freq_manazine = freq_dict(magazine)
#     freq_ran = freq_dict(ransomNote)

#     for ch, freq in freq_ran.items():
#         try:
#             if freq_manazine[ch] >= freq:
#                 continue
#             else:
#                 return False
#         except:
#             return False
#     return True

from collections import Counter
def canConstruct(ransomNote, magazine):
    rc = Counter(ransomNote)
    mc = Counter(magazine)

    for ch, freq in rc.items():
        if mc[ch] <= freq:
            return False
    return True



ransomNote = "aa"
magazine = "abaa"
print(canConstruct(ransomNote, magazine))