def generateMatrix(n):
    if n == 1:
        return [[1]]

    rows = columns = n
    left = 0
    right = columns - 1
    up = 0
    down = rows - 1

    # initialize matrix
    # matrix = n*[n*[0]] # n identical lists
    matrix = [n*[0] for i in range(n)] # n different lists

    i = 1
    while i <= n*n:
        # right to left
        for col in range(left, right + 1):
            matrix[up][col] = i
            i += 1
        up += 1
        # downwards
        for row in range(up, down+1):
            matrix[row][right] = i
            i += 1
        right -= 1
        # right to left
        for col in range(right, left-1, -1):
            matrix[down][col] = i
            i += 1
        down -= 1
        # upwards
        for row in range(down, up-1, -1):
            matrix[row][left] = i
            i += 1
        left += 1

    return matrix




n = 3
print(generateMatrix(n))