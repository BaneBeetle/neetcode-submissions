class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for value in nums:
            if value in seen:
                return True
            else:
                seen.add(value)
        
        return False
