class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        
        smallest = float('inf')

        # 1 2 3 3 5 6
        ptr1 = 0
        ptr2 = k - 1

        while ptr2 < len(nums):

            smallest = min(smallest, nums[ptr2] - nums[ptr1])

            ptr2 += 1
            ptr1 += 1
        
        return smallest
