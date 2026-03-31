class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we should set 2 pointers for this problem, left is min, right is max
        # we add to result, if result is smaller than target, move min to the right, otherwise, move max to left, else it is equal, return the result
        # that is the standard way to solve it, one can argue that using binary search is a better way, but it isn't as we can miss it out of our interval
        left = 0
        right = len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1
        return -1
        