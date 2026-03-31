class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def bfs(x, y):
            area = 0
            grid[x][y] = 0
            island = deque([(x, y)])
            while island:
                r, c = island.popleft()
                area += 1
                for dr, dc in directions:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < m and 0 <= uc < n and grid[ur][uc] == 1:
                        grid[ur][uc] = 0
                        island.append((ur, uc))
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        return maxArea

        