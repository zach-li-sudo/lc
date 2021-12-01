# dp sol, tc: o(mn), sc: o(1)
def updateMatrix(mat):
    if len(mat) == 0:
        return []
    R, C = len(mat), len(mat[0])
    for r in range(R):
        for c in range(C):
            if mat[r][c] > 0:
                up = mat[r-1][c] if r > 0 else math.inf
                left = mat[r][c-1] if c > 0 else math.inf
                mat[r][c] = min(up, left) + 1
        
    for r in range(R-1, -1, -1):
        for c in range(C-1, -1, -1):
            if mat[r][c] > 0:
                down = mat[r+1][c] if r < R - 1 else math.inf
                right = mat[r][c+1] if c < C - 1 else math.inf
                mat[r][c] = min(mat[r][c], down+1, right+1)
    
    return mat




# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
# print(updateMatrix(mat))
updateMatrix(mat)
