"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        days = 0
        start_times = []
        end_times = []

        for interval in intervals:
            start_times.append(interval.start)
            end_times.append(interval.end)
        
        start_times.sort()
        end_times.sort()

        ptr1 = 0
        ptr2 = 0
        current_days = 0

        while ptr1 < len(start_times):
            if start_times[ptr1] < end_times[ptr2]:
                current_days += 1
                ptr1 += 1
            else:
                # whenever our start time is more
                current_days -= 1
                ptr2 += 1

            days = max(days, current_days)

        return days






        


