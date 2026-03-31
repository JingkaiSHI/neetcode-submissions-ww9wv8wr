class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            result = max(result, w * h)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1


        return result
        