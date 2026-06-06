"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if not intervals:
        #     return True
        # n = len(intervals)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         a, b = intervals[i], intervals[j]
        #         if a.start < b.end and b.start < a.end:
        #             return False
        # return True

        # time: O(n^2)
        # space: O(1)

        intervals.sort(key = lambda i: i.start)
        for i in range(len(intervals) - 1):
            i1 = intervals[i]
            i2 = intervals[i+1]
            if i1.end > i2.start:
                return False
        return True
