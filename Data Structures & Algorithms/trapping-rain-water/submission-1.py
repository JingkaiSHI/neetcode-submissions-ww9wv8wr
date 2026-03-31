class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftHeight, rightHeight = height[l], height[r]
        result = 0
        while l < r:
            if leftHeight < rightHeight:
                l += 1
                leftHeight = max(leftHeight, height[l])
                result += leftHeight - height[l]
            else:
                r -= 1
                rightHeight = max(rightHeight, height[r])
                result += rightHeight - height[r]
        return result

        