def searchMatrix(matrix, target):
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False
    flatten = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            flatten.append(matrix[i][j])
    
    flatten.sort()
    lo = 0
    hi = len(flatten) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if flatten[mid] == target:
            return True
        elif flatten[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return False
    
    




matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 24
print(searchMatrix(matrix, target))