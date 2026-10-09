"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        previous_end = None
        for value in intervals:
            current_start = value.start
            current_end = value.end

            if not previous_end:
                # If we are just beginning..
                previous_end = current_end
            else:
                # Comparison logic here
                if current_start < previous_end:
                    return False
                previous_end = current_end

        return True
            

