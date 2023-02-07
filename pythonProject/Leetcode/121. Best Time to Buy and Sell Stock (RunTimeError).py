class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        count = len(prices) - 1
        if prices.sort(reverse=True) == prices:
            return 0
        else:
            while count > 0:
                if prices[count] > min(prices[: count]):
                    profit = max(profit, prices[count] - min(prices[: count]))
                count -= 1
            return profit





print(Solution().maxProfit([7,1,5,3,6,4]))