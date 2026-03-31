class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we have this inspiration from previous graph problem: we can do a multi-source BFS for this one, each rotting orange is a starting point
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        min_time = 0
        # scan through the array to find sources
        todo = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    todo.append((i, j, 0))
        

        # clean up the todo list by floodfilling the grid
        while todo:
            r, c, time = todo.popleft()
            min_time = max(min_time, time)
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if 0 <= ur < m and 0 <= uc < n and grid[ur][uc] == 1:
                    # it is a valid grid with a fresh orange, make it rot
                    grid[ur][uc] = 2
                    todo.append((ur, uc, time + 1))

        # look at the rotten grid to see if there are anything alive, if yes, return -1
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
        return min_time
        