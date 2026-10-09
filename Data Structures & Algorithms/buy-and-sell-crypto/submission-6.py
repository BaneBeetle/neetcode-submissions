class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr = 0
        r_ptr = 1

        max_profit = 0


        while r_ptr < len(prices):
            
            if prices[l_ptr] < prices[r_ptr]:
                # will run whenever right is more expensive
                profit = prices[r_ptr] - prices[l_ptr]

                if max_profit < profit:
                    max_profit = profit

            else:
                # will only run if right side is smaller, meaning we found a new local minimum
                l_ptr = r_ptr
            
            r_ptr += 1
        


        return max_profit

        


 
        