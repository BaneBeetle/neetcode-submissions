class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # what will do? [-4, -1, -1, 0, 1, 2]

        # a + b + c = 0

        # a = -(b + c) Two Sum!
        # Where a is our target, b and c we need to figure out

        ret = []

        a_history = set()

        index1 = 0 # in charge of a

        while index1 < len(nums):

            if (index1 + 2) >= len(nums):
                return ret
 
            elif nums[index1] in a_history:
                index1 += 1
                continue
            else:
                a_history.add(nums[index1])

                a = nums[index1]

                index2 = index1 + 1
                index3 = len(nums) -1 # [-4, -1, -1, 0, 1, 2] a = -4, index2 -> -1, index3 -> 2

                # two-sum
                # a = -(b + c) Two Sum!
                while index3 > index2:
                    b = nums[index2]
                    c = nums[index3]
                    s = a + b + c

                    
                    if s < 0:
                        index2 += 1
                    elif s > 0:
                        index3 -= 1
                    else:
                        # will occur whenever we have reached our target
                        ret.append([a, b, c])
                        index2 += 1

                        while (nums[index2] == nums[index2 - 1]) and index2 < index3:
                            index2 += 1



        return ret
