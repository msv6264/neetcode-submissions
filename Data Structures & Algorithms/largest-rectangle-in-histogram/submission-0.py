class Solution:
    def largestRectangleArea(self, hts: List[int]) -> int:
        maxAr = 0
        stk = []

        for i, h in enumerate(hts):
            strt = i 

            while stk and stk[-1][1] > h:
                idx, ht = stk.pop()
                maxAr = max(maxAr, ht * (i - idx))
                strt = idx

            stk.append((strt, h))

        for i, h in stk:
            maxAr = max(maxAr, h * (len(hts) - i))

        return maxAr