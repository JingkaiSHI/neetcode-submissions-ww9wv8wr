class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def helper(val):
            if val == 1:
                return True
            if val in seen:
                return False
            
            seen.add(val)
            nxt = 0
            while val > 0:
                cur = val % 10
                nxt += cur ** 2
                val = val // 10
            return helper(nxt)
        return helper(n)
        