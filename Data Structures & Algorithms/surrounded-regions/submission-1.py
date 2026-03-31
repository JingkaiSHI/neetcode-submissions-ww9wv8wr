class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        todo = deque([])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        todo.append((i, j))
        safe = set()
        while todo:
            r, c = todo.popleft()
            safe.add((r, c))
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if 0 <= ur < m and 0 <= uc < n and board[ur][uc] == 'O':
                    if (ur, uc) not in safe:
                        todo.append((ur, uc))
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in safe and board[i][j] == 'O':
                    board[i][j] = 'X'
