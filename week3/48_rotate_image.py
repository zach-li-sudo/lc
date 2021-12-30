class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(R):
            matrix[r].reverse()



matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.rotate(matrix))