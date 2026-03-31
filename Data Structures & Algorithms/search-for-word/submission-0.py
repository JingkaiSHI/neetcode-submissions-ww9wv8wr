class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        def backtrack(i, r, c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or word[i] != board[r][c] or board[r][c] == "#":
                return False
            board[r][c] = "#"
            for dr, dc in directions:
                ur, uc = r + dr, c + dc
                if backtrack(i + 1, ur, uc):
                    return True
            board[r][c] = word[i]
            return False
        for i in range(m):
            for j in range(n):
                if backtrack(0, i, j):
                    return True
        return False
        