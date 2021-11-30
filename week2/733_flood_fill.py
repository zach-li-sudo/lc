class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # recursive
        if image is None:
            return None

        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if image[sr][sc] == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
        dfs(sr, sc)
        return image

    
    # BFS
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image

    # DFS
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            dfs(sr, sc)
        return image




image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

sol = Solution()
sol.floodFill(image, sr, sc, newColor)