"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        previous_end = None
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if previous_end:
                if previous_end > interval.start:
                    return False
            
            previous_end = interval.end
        
        return True