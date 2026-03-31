class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        maxLen = 1
        for num in numSet:
            if num + 1 in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
        