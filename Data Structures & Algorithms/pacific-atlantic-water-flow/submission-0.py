class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        pacific = deque([])
        atlantic = deque([])
        for i in range(m):
            pacific.append((i, 0))
            atlantic.append((i, n - 1))

        for j in range(n):
            pacific.append((0, j))
            atlantic.append((m - 1, j))
        
        while pacific:
            r, c = pacific.popleft()
            pac[r][c] = True
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if 0 <= ur < m and 0 <= uc < n and not pac[ur][uc] and heights[ur][uc] >= heights[r][c]:
                    pacific.append((ur, uc))
        
        while atlantic:
            r, c = atlantic.popleft()
            atl[r][c] = True
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if 0 <= ur < m and 0 <= uc < n and not atl[ur][uc] and heights[ur][uc] >= heights[r][c]:
                    atlantic.append((ur, uc))
        result = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] == True and atl[i][j] == True:
                    result.append([i, j])
        return result
        