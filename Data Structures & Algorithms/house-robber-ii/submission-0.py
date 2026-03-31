class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        r1, r2 = 0, 0
        for num in nums:
            newR = max(r1 + num, r2)
            r1 = r2
            r2 = newR
        return r2
        