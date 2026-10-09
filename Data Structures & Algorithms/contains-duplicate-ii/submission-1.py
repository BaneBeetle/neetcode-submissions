class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ptr1 = 0
        

        while ptr1 < len(nums):
            ptr2 = ptr1 + 1
            while ptr2 < len(nums):
                if nums[ptr1] == nums[ptr2] and abs(ptr1 - ptr2) <= k:
                    return True
                
                ptr2 += 1


            ptr1 += 1
        
        return False