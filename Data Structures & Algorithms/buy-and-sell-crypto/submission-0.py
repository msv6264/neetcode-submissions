class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProf = 0

        for i in range(len(prices) - 1):
            j = i + 1
            while j < len(prices):
                if prices[j] > prices[i]:
                    mProf = max(mProf, (prices[j] - prices[i]))
                j += 1

        return mProf