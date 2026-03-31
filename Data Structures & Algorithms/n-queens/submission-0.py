class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        posDiag = [False] * (n * 2)
        negDiag = [False] * (n * 2)
        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                method = ["".join(row) for row in board]
                result.append(method)
                return
            for c in range(n):
                if cols[c] or posDiag[r + c] or negDiag[r - c + n]:
                    continue
                # append to path
                cols[c] = True
                posDiag[r + c] = True
                negDiag[r - c + n] = True
                board[r][c] = "Q"
                
                backtrack(r + 1)
                board[r][c] = "."
                negDiag[r - c + n] = False
                posDiag[r + c] = False
                cols[c] = False
        backtrack(0)
        return result
        