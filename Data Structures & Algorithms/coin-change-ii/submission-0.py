class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]
            
            result = 0
            if a >= coins[i]:
                result = dfs(i + 1, a)
                result += dfs(i, a - coins[i])
            
            memo[i][a] = result
            return result
        return dfs(0, amount)
        