class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lresult = [1] * len(nums)
        rresult = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            lresult[i] = lresult[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            rresult[j] = rresult[j + 1] * nums[j + 1]
        for k in range(len(nums)):
            result[k] = lresult[k] * rresult[k]
        return result
        