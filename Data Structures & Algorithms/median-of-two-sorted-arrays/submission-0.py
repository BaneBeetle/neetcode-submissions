class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums2 + nums1
        nums3.sort()
        print(nums3)

        if len(nums3) % 2 != 0:
            return (nums3[len(nums3)//2])
        else:
            val1 = nums3[len(nums3)//2]
            val2 = nums3[len(nums3)//2 - 1]
            print(val1)
            print(val2)
            return (val1 + val2) / 2
        