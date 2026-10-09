class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        print(intervals)
        remove_counter = 0 # this will contain values we don't want to leave in the last return statements
        
        previous_start = intervals[0][0]
        previous_end = intervals[0][1] # the first end time

        for interval in intervals[1:]:
            current_start = interval[0]
            current_end = interval[1]

            if previous_end > current_start:

                if current_end >= previous_end:
                    remove_counter += 1

                else:
                    # previous one was bigger
                    remove_counter += 1
                    previous_end = current_end
                    previous_start = current_start
            else:
                previous_end = current_end
                previous_start = current_start
        
        return remove_counter