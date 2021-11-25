# sol 1. brute force
def matrixReshape(mat, r, c):
    flatten = [i for sublist in mat for i in sublist]
    if r*c != len(flatten):
        return mat

    reshaped = []
    for i in range(r):
        reshaped.append(flatten[i*c:(i+1)*c])
    return reshaped

    

# def matrixReshape(mat, r, c):
#     pass



mat = [[1,2],[3,4]]
r = 2
c = 2

print(matrixReshape(mat, r, c))