class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # grab the price and their indexes
        lst = []

        for index, price in enumerate(prices):
            lst.append((price, index))
        
        # sort them from least expensive -> most expensive (tie breaking scenarios, python will auto index)
        lst.sort() # someting like this: [(1, 1), (3, 3), (4, 5), (5, 2), (6, 4), (7, 0)] (price, index)


        # Create two pointers
        ptr1 = 0
        ptr2 = len(lst) - 1 # in charge of being in the back

        # use these pointers to compare values in the sorted list

        ret = []

        while ptr1 < len(lst):

            if lst[ptr1][1] < lst[ptr2][1]:
                # ptr1's index is less, so we should sell
                ret.append(lst[ptr2][0] - lst[ptr1][0])
                ptr2 -= 1
            
            # If the above if statement does not execute, that means ptr1's index is larger meaning we can't sell
            elif ptr1 == ptr2:
                # this means ptr1 is the issue, so move it and move ptr2 all the way to the back
                ptr1 += 1
                ptr2 = len(lst) - 1
            else:
                ptr2 -= 1
        
        ret.sort()
        print(ret)

        if ret == []:
            return 0

        return ret[-1]

        