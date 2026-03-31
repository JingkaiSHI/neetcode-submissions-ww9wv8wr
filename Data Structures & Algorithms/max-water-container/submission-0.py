class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        left = 0
        right = len(heights) - 1
        best = 0
        while left < right:
            cur = (right - left) * min(heights[left], heights[right])
            if cur > best:
                best = cur
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return best
        