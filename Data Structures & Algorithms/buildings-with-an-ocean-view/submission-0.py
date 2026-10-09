class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        # Keep popping from the stack

        # stack for height, stack for index


        indeces = []
        stack = []

        ptr = 0

        while ptr < len(heights):

            while len(stack) > 0 and (heights[ptr] >= stack[-1]):
                stack.pop()
                indeces.pop()
            
            stack.append(heights[ptr])
            indeces.append(ptr)

            ptr += 1
        

        return indeces