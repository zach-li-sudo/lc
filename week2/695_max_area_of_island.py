class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        seen = set()
        R, C = len(grid), len(grid[0])
        def area(r,c):
            if not (0 <= r < R and 0 <= c < C and (r,c) not in seen and grid[r][c]):
                # in brackets: valid r,c , (r,c) not visited, grid[r][c] is 1
                # if not satisfied, contribute 0
                return 0
            seen.add((r,c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c+1) + area(r, c-1))

        return max(area(r, c) for c in range(C) for r in range(R))