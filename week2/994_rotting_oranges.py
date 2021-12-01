import collections
# bfs
def orangesRotting(grid):
    if grid is None:
        return -1
    R, C = len(grid), len(grid[0])
    max_iter = R + C

    # Step 1. init
    fresh_oranges = 0
    queue = collections.deque([])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: queue.append((r, c))
            if grid[r][c] == 1: fresh_oranges += 1
    queue.append((-1,-1))

    # step 2
    step = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        r, c = queue.popleft()
        if r == -1:
            step += 1
            if queue:
                queue.append((-1,-1))
        else: # rotten orange
            for d in directions:
                neighbor_r, neighbor_c = r + d[0], c + d[1]
                if 0 <= neighbor_r < R and 0 <= neighbor_c < C:
                    if grid[neighbor_r][neighbor_c] == 1:
                        grid[neighbor_r][neighbor_c] = 2
                        fresh_oranges -= 1
                        queue.append((neighbor_r, neighbor_c))
    
    return step if fresh_oranges == 0 else -1


# grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))

    





