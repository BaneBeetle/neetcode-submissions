class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import Counter

        nums_hash = Counter(nums)

        ptr = 0

        while ptr < len(nums):
            desired_value = target - nums[ptr]

            if nums_hash[desired_value] > 0:
                index = nums.index(desired_value)
                if ptr != index:
                    return sorted([ptr, index])

            ptr += 1