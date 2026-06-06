"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted(i.start for i in intervals)   
        end = sorted(i.end for i in intervals)

        res, count = 0, 0
        s, e = 0, 0

        while s < n:
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res

        # time: O(n log n)
        # space: O(n)
