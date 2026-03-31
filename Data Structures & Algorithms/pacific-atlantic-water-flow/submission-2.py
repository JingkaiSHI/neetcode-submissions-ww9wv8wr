class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        pacific = deque([])
        atlantic = deque([])

        def bfs(todo, ocean):
            while todo:
                r, c = todo.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < m and 0 <= uc < n and not ocean[ur][uc] and heights[ur][uc] >= heights[r][c]:
                        todo.append((ur, uc))
        
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))
        
        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m - 1, j))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        result = []
        for x in range(m):
            for y in range(n):
                if pac[x][y] and atl[x][y]:
                    result.append([x, y])
        return result