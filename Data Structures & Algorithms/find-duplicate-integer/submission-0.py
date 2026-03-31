class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Easy solve: keep a hashmap for all numbers we encountered
        # but this will be O(n) in terms of space
        # Clue is that there is only 1 number that appears 2 or more times
        # solution: negative marking or fast and slow pointer:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1
        