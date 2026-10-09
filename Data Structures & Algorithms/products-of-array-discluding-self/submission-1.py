class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        ret = [0] * len(nums)

        # prefix creation
        ptr1 = 0
        while ptr1 < len(nums):
            if ptr1 == 0:
                prefix[ptr1] = nums[ptr1]
            else:
                prefix[ptr1] = nums[ptr1] * prefix[ptr1 - 1]
            ptr1 += 1
        
        # postfix creation
        ptr2 = len(nums) - 1
        while ptr2 >= 0:
            if ptr2 == len(nums) - 1:
                postfix[ptr2] = nums[ptr2]
            else:
                postfix[ptr2] = nums[ptr2] * postfix[ptr2 + 1]

            ptr2 -= 1

        # Put it all in an array
        ptr3 = 0
        while ptr3 < len(ret):
            if ptr3 == 0:
                ret[ptr3] = postfix[ptr3 + 1]
            elif ptr3 == len(ret) - 1:
                ret[ptr3] = prefix[ptr3 - 1]
            else:
                ret[ptr3] = prefix[ptr3 - 1] * postfix[ptr3 + 1]
            
            ptr3 += 1
            
        return ret
