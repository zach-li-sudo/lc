from itertools import combinations, permutations
class Solution:
    def combine(self, n: int, k: int):
        # terminator

        return [list(c) for c in itertools.combinations(list(range(1,n+1)), k)]
        

n = 5
k = 3

sol = Solution()
print(sol.combine(n, k))


comb = combinations(list(range(1, n+1)), k)
print([list(c) for c in comb])