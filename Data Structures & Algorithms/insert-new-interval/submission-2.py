class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort()
        print(intervals)

        ret = []

        previous_end = intervals[0][1]
        previous_start = intervals[0][0]

        for interval in intervals[1:]:
            current_start = interval[0]
            current_end = interval[1]

            if previous_end >= current_start:
                previous_end = max(previous_end, current_end)
            else:
                ret.append([previous_start, previous_end])
                previous_start = current_start
                previous_end = current_end
        
        ret.append([previous_start, previous_end])

        return ret


        
        

