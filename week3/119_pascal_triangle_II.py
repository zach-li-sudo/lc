class Solution:
    def getRow(self, rowIndex):
        row = [1]
        if rowIndex == 1:
            return row
        row = [1,1]
        while len(row) < rowIndex:
            for i in range(len(row) - 1):
                row[i] = row[i] + row[i+1]
            row.insert(0, 1)
        return row


rowIndex = 5
sol = Solution()
print(sol.getRow(rowIndex))