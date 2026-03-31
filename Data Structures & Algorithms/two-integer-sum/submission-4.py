class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            lookup[nums[i]] = i
        
        for j in range(len(nums)):
            counter = target - nums[j]
            if counter in lookup and lookup[counter] != j:
                if lookup[counter] < j:
                    return [lookup[counter], j]
                else:
                    return [j, lookup[counter]]
        return [-1, -1]
        