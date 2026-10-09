class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_dict = {} # Values that we have seen

        # since there is exactly 1 pair of indices, we only need to go through num list once and check back if we have seen "special value"
        # what is special value? its target - current val
        index = 0 
        for value in nums:
            special_num = target - value

            if special_num in num_dict:
                # If we ever reach here, we will have the index of both desired numbers
                # 7, 4 <- stored first in the dictionary, the one we are currently on right now will always be more since we are look at "past"
                # elements with a lower index
                return [num_dict[special_num], index]
            else:
                num_dict[value] = index
            
            index += 1
        
        return []
