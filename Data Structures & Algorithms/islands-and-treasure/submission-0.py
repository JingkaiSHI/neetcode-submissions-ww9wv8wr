class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # key insights:
        # - the chosen value for 0 about a treasure chest is quite smart
        # - if a location's value is already smaller than what we have, we don't update it (it is either another chest itself, or it is closer to another chest)
        # - we only need to flood fill times in terms of number of chests
        # - it is a flood fill in fixed directions, it makes sense to create a direction array
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])

        def update(i, j):
            todo = deque([(i, j, 0)])
            while todo:
                # while we still have a node we can update
                r, c, distance = todo.popleft()
                grid[r][c] = min(distance, grid[r][c])

                for dr, dc in directions:
                    ur, uc = r + dr, c + dc
                    if 0 <= ur < m and 0 <= uc < n and grid[ur][uc] > distance:
                        todo.append((ur, uc, distance + 1))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    update(i, j)
        