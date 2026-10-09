class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}


        for num in nums:
            if seen.get(num) == None:
                seen[num] = 1
            else:
                return True

        return False
