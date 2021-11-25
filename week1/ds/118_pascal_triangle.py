def generate(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    pascal = [[1]]

    for num in range(2, numRows+1):
        prev = pascal[-1]
        current = [0 for _ in range(num)]
        current[0], current[-1] = 1, 1
        for j in range(len(prev)-1):
            current[j+1] = prev[j] + prev[j+1]
        
        pascal.append(current)

    return pascal


numRows = 6
print(generate(numRows))