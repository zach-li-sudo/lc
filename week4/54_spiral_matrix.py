# sol 1. move matrix border
# def spiralOrder(matrix):
#     result = []
#     rows, columns = len(matrix), len(matrix[0])
#     up = left = 0
#     down = rows - 1
#     right = columns - 1

#     while len(result) < rows * columns:
#         # traverse from left to right
#         for col in range(left, right+1):
#             result.append(matrix[up][col])
        
#         # traverse downwards
#         for row in range(up + 1, down + 1):
#             result.append(matrix[row][right])
        
#         # traverse from right to left:
#         if up != down:
#             for col in range(right - 1, left - 1, -1):
#                 result.append(matrix[down][col])
        
#         #
#         if left != right:
#             for row in range(down - 1, up, -1):
#                 result.append(matrix[row][left])

#         left += 1
#         right -= 1
#         up += 1
#         down -= 1

#     return result



# sol 2. mark visited elements
def spiralOrder(matrix):
    VISITED = 1000
    rows, columns = len(matrix), len(matrix[0])
    # directions
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # right, down, left, up
    # initial direction: moving right
    current_direction = 0
    change_direction = 0

    row = col = 0
    result = [matrix[0][0]]
    matrix[0][0] = VISITED

    while change_direction < 2:
        while True:
            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]

            # break if the next step is out of bound
            if not (0 <= next_row < rows and 0 <= next_col < columns):
                break
            if matrix[next_row][next_col] == VISITED:
                break

            change_direction = 0
            row, col = next_row, next_col
            result.append(matrix[row][col])
            matrix[row][col] = VISITED

        current_direction = (current_direction + 1) % 4
        change_direction += 1
    
    return result




matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))