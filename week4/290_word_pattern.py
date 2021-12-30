def wordPattern(pattern, s):
    s_list = s.split(' ')
    if len(pattern) != len(s_list):
        return False
    hm = dict()
    for i in range(len(pattern)):
        p = pattern[i]
        word = s_list[i]
        if p in hm:
            if hm[p] != word:
                return False
        elif p not in hm:
            if word not in hm.values():
                hm.update({p: word})
            else:
                return False
    return True


pattern = "abba"
s = "dog dog dog dog"

# pattern = "aaa"
# s = "aa aa aa aa"

# pattern = "abba"
# s ="dog cat cat dog"
print(wordPattern(pattern, s))