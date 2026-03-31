from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            todo = deque([(i, j)])
            while todo:
                r, c = todo.popleft()
                grid[r][c] = "0"
                for dr, dc in dirs:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < m and 0 <= uc < n and grid[ur][uc] == "1":
                        todo.append((ur, uc))
        result = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    bfs(x, y)
                    result += 1
        return result

            
        