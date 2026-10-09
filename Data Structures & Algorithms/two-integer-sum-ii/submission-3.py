class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # target - current number = what we need to find
        # 3 - 1 = 2
        # Does it exist in the list? If it does, what index is it?
        # sorted, non-decreasing order

        index1 = 0

        while index1 < len(numbers):
            first_num = numbers[index1]
            index2 = 0
            while index2 < len(numbers):
                if index1 == index2:
                    index2 += 1
                else:
                    second_num = numbers[index2]

                    if (first_num + second_num) == target:
                        return [index1 + 1, index2 + 1]
                    else:
                        index2 += 1

            index1 += 1
        
        return []
