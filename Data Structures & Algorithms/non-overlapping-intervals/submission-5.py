class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i: i[0])
        n = len(intervals)
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if prevEnd > start:
                prevEnd = min(end, prevEnd)
                res += 1
            else:
                prevEnd = end

        return res

        # time: O(nlogn)
        # space: O(1)