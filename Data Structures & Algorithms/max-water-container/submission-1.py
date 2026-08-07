class Solution:
    def maxArea(self, hts: List[int]) -> int:
        n = len(hts)
        i, j = 0, n-1
        mxAr = 0
        currAr = 0

        while i < j:
            wid = j - i
            ht = min(hts[i], hts[j])
            currAr = wid * ht
            mxAr = max(mxAr, currAr)

            if ht == hts[i] and hts[i] != hts[j]:
                i += 1
            else:
                j -= 1

        return mxAr