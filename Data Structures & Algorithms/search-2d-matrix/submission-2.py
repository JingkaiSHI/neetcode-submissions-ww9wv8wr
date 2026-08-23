# think out loud:
# 2D matrix, m by n
# target
# each row, each int is non-decreasing
# find a way to encode every index to search in a "flattened" int array, regress back to normal Binary search
# given int i, 0 <= i <= (m * n - 1)
# x = i // n, y = i % n
# ie. i = 11, m = 3, n = 4, x = 2, y = 3, which is the exact index of a i
# map a projection from [i][j] to x

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n - 1)

        while l <= r:
            mid = (l + r) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False

        