class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1) Compare all relevant combinations of bars
        # 1a) 1 ptr start at the beginning, and one start at the end
        # 2) Calculation -> area = distance * smallest bar

        index1 = 0
        index2 = len(heights) - 1
        max_seen = 0

        while index1 < index2:
            distance = index2 - index1
            current_area = distance * min(heights[index1], heights[index2])

            if current_area > max_seen:
                max_seen = current_area
            
            if heights[index1] < heights[index2]:
                index1 += 1
            elif heights[index1] > heights[index2]:
                index2 -=1
            else:
                # same value
                # choose an arbitrary tie breaker
                index1 += 1
        
        return max_seen
