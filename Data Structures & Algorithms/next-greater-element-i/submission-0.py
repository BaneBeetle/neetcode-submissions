class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Maybe we can construct a hasmap of nums1
        # Maybe we can use enumerate?

        # Need to return the value or -1, no index
        # Build naive solution first:

        ptr1 = 0
        

        ret = [-1] * len(nums1)

        while ptr1 < len(nums1):
            ptr2 = nums2.index(nums1[ptr1])

            while ptr2 < len(nums2):
                if nums2[ptr2] > nums1[ptr1]:
                    ret[ptr1] = nums2[ptr2]
                    break
                else:
                    ptr2 += 1

            ptr1 += 1

        return ret