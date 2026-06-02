class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # bruteforce way is to check every combinations of numbers, adding seen triplets to set
        # but this is too chaotic way to find out the solution, so we can do a bit improvement on top of it
        # fix 1 value at a time, then the problem is to search for candidates that solves for a 2Sum
        # 2Sum itself can be a bit too much for repeated usage, so we can sort it to make it faster
        # hence the algorithm logic should look like this
        result = []
        # 1. we sort the nums in place in increasing order
        nums.sort()
        # 2. for each potential fixing value we make it the current pivot index i (we can stop if we have seen this value before or this value is greater than 0)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 3. from i + 1 to end of array, we try to find j and k that adds up to -nums[i] (2Sum in sorted array)
            j, k = i + 1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current > 0:
                    k -= 1
                    while 0 < k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        # avoid duplicate
                        k -= 1
                elif current < 0:
                    j += 1
                    while len(nums) - 1 >= j > i + 1 and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    # 4. when we find one, we want to move the pointer either forward or backward to avoid duplicate as it is sorted
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while len(nums) - 1 >= j > i + 1 and nums[j] == nums[j - 1]:
                        j += 1
                    while 0 <= k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        k -= 1
        return result

        
        