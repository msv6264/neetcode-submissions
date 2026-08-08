class Solution:
    def trap(self, hts: List[int]) -> int:
        n = len(hts)
        maxLft, maxRght = [-1]*n, [-1]*n

        for i in range(1, n):
            maxLft[i] = max(maxLft[i - 1], hts[i - 1])
        
        for i in range(n-2, -1, -1):
            maxRght[i] = max(maxRght[i + 1], hts[i + 1])

        res = 0
        for i in range(n):
            res += max(0, min(maxLft[i], maxRght[i]) - hts[i])

        return res