class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                n = n + prices[i+1] - prices[i]
                i = i + 1
        return n