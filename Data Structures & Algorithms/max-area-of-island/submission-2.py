class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0

        def bfs(x, y):
            cur_area = 0
            todo = deque([(x, y)])
            grid[x][y] = 0
            while todo:
                r, c = todo.popleft()
                cur_area += 1
                for dr, dc in dirs:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < m and 0 <= uc < n and grid[ur][uc] == 1:
                        grid[ur][uc] = 0
                        todo.append((ur, uc))
            return cur_area


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    result = max(result, area)
        return result