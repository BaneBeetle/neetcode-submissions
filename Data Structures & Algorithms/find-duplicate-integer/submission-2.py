class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        og_slow = 0
        fast = 0
        
        while True:
            og_slow = nums[og_slow]
            fast = nums[fast]
            fast = nums[fast]
            

            if og_slow == fast:
                break
        

        slow = 0
        while True:
            slow = nums[slow]
            og_slow = nums[og_slow]

            if og_slow == slow:
                break
        
        return og_slow

