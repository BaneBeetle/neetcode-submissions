class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ret = [1] * len(nums)
        
        # prefix logic
        prefix = []
        ptr1 = 0

        #postfix logic
        postfix = [1] * len(nums)
        ptr2 = len(nums) - 1

        # prefix first O(n) + postfix O(n) -> O(n)

        prev = None

        while ptr1 < len(nums): # O(n)

            current_val = nums[ptr1]

            if prev is None:
                # When we are at the very beginning
                prev = current_val
                prefix.append(current_val)
            else:
                prefix.append(prev * current_val)
                prev = prev * current_val

            ptr1 += 1
        
        prev2 = None
        while ptr2 >= 0:

            current_val = nums[ptr2]

            if prev2 is None:
                prev2 = current_val
                postfix[ptr2] = current_val
            else:
                postfix[ptr2] = current_val * prev2
                prev2 = current_val * prev2

            ptr2 -= 1
        
        counter = 0
        while counter < len(ret):
            if counter == 0:
                # beginning of the list
                ret[counter] = postfix[counter + 1]
            elif counter == (len(ret) - 1):
                # last element
                ret[counter] = prefix[counter - 1]
            else:
                ret[counter] = postfix[counter + 1] * prefix[counter - 1]
            
            counter += 1

        return ret
  