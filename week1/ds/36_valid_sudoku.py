def isValidSudoku(board):
    for row in range(9):
        box = board[row]
        if not valid_box(box):
            return False
    
    for col in range(9):
        box = [b[col] for b in board]
        if not valid_box(box):
            return False

    for i in range(3):
        for j in range(3):
            box = [board[x][y] for x in range(3*i, 3*(i+1)) for y in range(3*j, 3*(j+1))]
            if not valid_box(box):
                return False
    return True


def valid_box(box):
    nums = box[:]
    while "." in nums:
        nums.remove(".")
    # no duplicate: valid, duplicate: invalid
    return len(set(nums)) == len(nums)



# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))