class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        cur_element = None
        cur_reps = 0
        for num in nums:
            if cur_element is None:
                nums[k] = num
                k += 1
                cur_element = num
                cur_reps = 1
            else:
                if num == cur_element:
                    if cur_reps < 2:
                        nums[k] = num
                        k += 1
                        cur_reps += 1
                else:
                    nums[k] = num
                    k += 1
                    cur_element = num
                    cur_reps = 1
        return k
        