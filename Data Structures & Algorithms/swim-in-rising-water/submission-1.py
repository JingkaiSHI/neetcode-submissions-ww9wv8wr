class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]] # time/maxheight, row, col
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit):
                    visit.add((nr, nc))
                    heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])
        