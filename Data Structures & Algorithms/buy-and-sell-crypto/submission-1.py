class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProf = 0
        b, s = 0, 1

        while s < len(prices):
            if prices[s] > prices[b]:
                prof = prices[s] - prices[b]
                mProf = max(mProf, prof)

            else:
                b = s
            s += 1

        return mProf