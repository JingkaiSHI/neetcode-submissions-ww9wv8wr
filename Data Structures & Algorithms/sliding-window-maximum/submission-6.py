from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        n = len(nums)
        if k == 1:
            return nums[:]  # every element is its own window max
        dq = deque()  # will store indices, nums[dq[i]] is non-increasing with i
        res = []

        for i, val in enumerate(nums):
            # 1) Pop indices from back while their values < current value
            while dq and nums[dq[-1]] < val:
                dq.pop()

            # 2) Append current index
            dq.append(i)

            # 3) Remove indices that are out of the current window (i - k + 1 is left bound)
            if dq[0] <= i - k:
                dq.popleft()

            # 4) Starting from i >= k-1 we have a full window, record the max
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

        