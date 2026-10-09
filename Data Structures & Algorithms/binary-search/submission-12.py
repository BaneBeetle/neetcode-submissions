class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 # Written to avoid overflow (Claude said good practice)

            result = nums[mid]

            if result == target:
                return mid
            elif result < target:
                # Move to the right
                left = mid + 1
            
            elif result > target:
                # Its to the left
                right = mid - 1
            
        
        return -1