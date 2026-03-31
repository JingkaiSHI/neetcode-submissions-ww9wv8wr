class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row is strictly larger than previous row
        # think from a 1-d perspective: map the index to x, y
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            a = l + (r - l) // 2
            x, y = a // n, a % n
            if target > matrix[x][y]:
                l = a + 1
            elif target < matrix[x][y]:
                r = a - 1
            else:
                return True
        
        return False
        