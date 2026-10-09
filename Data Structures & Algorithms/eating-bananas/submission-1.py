class Solution:

    def can_finish(self, k: int, piles: List[int], h: int) -> bool:
        # We obtain a rate of k
        # Loop through the entire thing, see if we can finish
        from math import ceil
        time = 0

        for value in piles:
            time += ceil(value / k)
        
        return time <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum k 

        left = 1 # Represents slowest/minimum we can eat
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            finish = self.can_finish(mid, piles, h)

            if finish:
                right = mid
            else:
                left = mid + 1
        
        return left

