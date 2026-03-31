class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        cur_best = r
        while l <= r:
            k = (r + l) // 2
            cur_count = 0
            for pile in piles:
                cur_count += (- (- pile // k))
            if cur_count > h:
                l = k + 1
            else:
                cur_best = k
                r = k - 1
        return cur_best
        