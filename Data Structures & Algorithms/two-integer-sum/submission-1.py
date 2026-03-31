class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_map = {}
        for i in range(len(nums)):
            sol_map[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in sol_map and i != sol_map[nums[i]]:
                return [i, sol_map[nums[i]]]

        """
        {
            4: 0
            3: 1
            2: 2
            1: 3
        }
        """