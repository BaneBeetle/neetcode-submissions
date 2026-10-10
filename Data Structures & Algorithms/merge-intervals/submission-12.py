class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for interval in intervals:
            if ret:
                previous_start = ret[-1][0]
                previous_end = ret[-1][1]

                if previous_end >= interval[0]:
                    ret[-1] = [min(previous_start, interval[0]), max(previous_end, interval[1])]
                else:
                    ret.append(interval)
            else:
                ret.append(interval)
        return ret

            
