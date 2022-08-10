class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        pro = 0
        min_price = 1e9

        for price in prices:
            min_price = min(price, min_price)
            pro = max(pro, price - min_price)


        return pro


print(Solution().maxProfit([2,4,1]))
