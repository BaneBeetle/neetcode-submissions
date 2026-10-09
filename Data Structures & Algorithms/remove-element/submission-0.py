class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = []

        for num in nums:
            if num != val:
                ret.append(num)
        for x in range(len(ret)):
            nums[x] = ret[x]
        return len(ret)