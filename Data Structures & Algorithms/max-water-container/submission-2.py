class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max = 0

        ptr1 = 0
        ptr2 = len(heights) - 1

        while ptr1 < ptr2:

            current_area = min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1)

            global_max = max(current_area, global_max)

            if heights[ptr1] > heights[ptr2]:
                ptr2 -= 1
            else:
                ptr1 += 1

        return global_max
