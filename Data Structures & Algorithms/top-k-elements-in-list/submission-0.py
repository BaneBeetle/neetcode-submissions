class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_table = {} # {num : occurances}


        for digit in nums:
            if digit not in frequency_table:
                frequency_table[digit] = 1
            else:
                frequency_table[digit] += 1
        
        freq_sorted = sorted(list(frequency_table.items()),key=lambda x: x[1], reverse=True) # Sorts it DESC order, second val is the freq

        counter = 0
        return_list = []
        while counter < k:

            return_list.append(freq_sorted[counter][0])

            counter += 1
        
        return return_list

