class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ret = []
        
        # First, lets sort nums
        nums.sort()

        # Ensure its sorted
        print(nums)

        # Create an outside pointer. Here we will have a pointer traversing left --> right
        # Then we will have L and R pointers squeezing.

        ptr = 0


        while ptr < len(nums):
            l = ptr + 1
            r = len(nums) - 1

            # l and r will squeeze

            while l < r:
                if nums[ptr] + nums[l] + nums[r] == 0:
                    ret.append([nums[ptr] , nums[l] , nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                # Now we must do smarter l r shift logic

                # [-4, -1, -1, 0, 1, 2]
                # I think if negative, move left.
                # If positive and too big, move right

                elif nums[ptr] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[ptr] + nums[l] + nums[r] > 0:
                    r -= 1
            while ptr + 1 < len(nums) and nums[ptr] == nums[ptr + 1]:
                ptr += 1
            ptr += 1

        print(ret)
        return ret

