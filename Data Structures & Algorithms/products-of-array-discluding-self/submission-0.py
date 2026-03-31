class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        left = 1
        for i in range(len(nums)):
            result[i] = result[i] * left
            left = left * nums[i]

        right = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * right
            right = right * nums[j]
        return result
        