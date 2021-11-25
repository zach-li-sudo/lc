# def searchMatrix(matrix, target):
#     m = len(matrix) # num of rows
#     n = len(matrix[0]) # num of cols

#     mi, mj = 0, m - 1
#     while mi < mj:
#         m_mid = mi + (mj - mi) // 2
#         if matrix[m_mid][-1] == target:
#             return True
#         elif matrix[m_mid][-1] < target:
#             mi = m_mid
#             if mi + 1 == mj:
#                 return mj
#         else:
#             mj = m_mid
#             if mi + 1 == mj:
#                 return mj
    
#     return mj


def searchMatrix(matrix, target):
    flatten = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
    if target in flatten:
        return True
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20

print(searchMatrix(matrix, target))