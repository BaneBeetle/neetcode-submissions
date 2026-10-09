class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # target - current number = what we need to find
        # 3 - 1 = 2
        # Does it exist in the list? If it does, what index is it?
        # sorted, non-decreasing order

        # first_num + second_num > target, the rest of the list does not matter

        ptr1 = 0
        ptr2 = len(numbers) - 1

        while ptr1 < ptr2:

            s = numbers[ptr1] + numbers[ptr2]

            # is it valid:
            if s == target:
                return [ptr1 + 1, ptr2 + 1]
            
            # if its not, we have 2 scenarios
            
            # when the sum is greater than target
            elif s > target:
                # This means that the number corresponding with ptr2 is too big
                ptr2 -= 1

            # when the sum is less than target
            else:
                ptr1 += 1

        return []
