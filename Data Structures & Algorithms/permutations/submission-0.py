class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(nums, i):
            if i == len(nums):
                result.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(nums, 0)
        return result
        