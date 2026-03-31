class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for num in nums:
            if num in visited:
                return True
            else:
                visited.append(num)
        return False
         