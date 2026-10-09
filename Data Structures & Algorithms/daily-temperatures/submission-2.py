class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # initialize a stack to remember indexes and temperatures
        stack = [] # will look like: [(0, 30), (1, 38), ...]
        output = [0] * len(temperatures) # will init an array of 0's. Covers when there are no days that are bigger than ith day

        for index, temp in enumerate(temperatures):
            # We want to keep popping until we find a temperature that is larger than our current temperature
            while stack and temp > stack[-1][1]:
                # this will run if the top is smaller than current
                index2, temp2 = stack.pop()
                difference = index - index2
                output[index2] = difference

            stack.append((index, temp)) # [(5, 40)]
        
        return output


