class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums[:]
        result = nums + nums2
        return result
        