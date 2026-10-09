class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            print("hi")
            return [intervals[0]]

        intervals.sort() # if there was a class interval, intervals.sort(key=lambda i: i.start)

        previous_start = intervals[0][0]
        previous_end = intervals[0][1]

        ret = []

        for interval in intervals[1:]:
            
            current_start = interval[0]
            current_end = interval[1]

            if previous_end >= current_start:
                previous_end = max(current_end, previous_end)


            else:
                ret.append([previous_start, previous_end])
                previous_start = current_start
                previous_end = current_end

        print(previous_start, previous_end)
        ret.append([previous_start, previous_end])
        return ret
        