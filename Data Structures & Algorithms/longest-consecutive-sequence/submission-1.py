class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0



        lookup = set(nums)

        highest = 0

        for num in nums:
            if (num - 1) not in lookup:
                counter = 1
                current_seq = 0
                flag = True

                while flag:

                    if (num + counter) in lookup:
                        current_seq += 1
                        counter += 1

                        if current_seq > highest:
                            highest = current_seq

                    else:
                        flag = False
                        counter = 0


        return highest + 1