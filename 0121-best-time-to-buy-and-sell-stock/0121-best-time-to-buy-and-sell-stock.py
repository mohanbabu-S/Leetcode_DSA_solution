class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        expect_res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            expect_res = max(expect_res, price - lowest)
        return expect_res