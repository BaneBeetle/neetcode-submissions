class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1) Which two bars should we choose?
        # 2) Calculation

        max_hold = 0

        # fill up d with all of the combinations with their areas
        # sort based on dict.values

        index1 = 0 # in charge of computing whats on the left half
            
        while index1 < len(heights) - 1:
            index2 = 0

            while index2 < len(heights):

                while index2 <= index1:
                    index2 += 1

                distance = index2 - index1
                current_held = distance * min(heights[index1], heights[index2])
                if current_held > max_hold:
                    max_hold = current_held
                index2 += 1
            
            index1 += 1
        
        return max_hold


            
