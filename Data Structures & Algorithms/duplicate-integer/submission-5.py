class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False
            
        from collections import Counter

        x = Counter(nums)
        
        return sorted(x.values(), reverse=True)[0] > 1
        