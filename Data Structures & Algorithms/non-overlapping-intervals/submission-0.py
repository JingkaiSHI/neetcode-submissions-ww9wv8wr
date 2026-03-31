class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # comparisons:
        # intervals[i][1] <= intervals[j][0] means i and j doesn't overlap
        # Sort the intervals in starting time
        intervals.sort()
        result = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                prevEnd = min(end, prevEnd)
        return result
        