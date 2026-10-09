class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        
        ptr = 0

        while ptr < len(nums1):
            if nums1[ptr] in nums2 and nums1[ptr] not in ret:
                ret.append(nums1[ptr])
            ptr += 1
        return ret
        