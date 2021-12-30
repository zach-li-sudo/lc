import itertools
class Solution:
    def letterCasePermutation(self, s):
        numbers = [str(i) for i in range(0,10)]
        letters_in_s = [ch.lower() for ch in s if ch.isalpha()]
        bin_masks = itertools.product([0,1], repeat=len(letters_in_s))

        
        letters_combs = []
        for mask in bin_masks:
            letters = ''
            for i in range(len(letters_in_s)):
                if mask[i] == 0:
                    letters += letters_in_s[i].lower()
                else:
                    letters += letters_in_s[i].upper()
                
            letters_combs.append(letters)

        print(letters_combs)
        res = []
        for comb in letters_combs:
            for i in range(len(s)):
                


s = "a1b2"
sol = Solution()
sol.letterCasePermutation(s)