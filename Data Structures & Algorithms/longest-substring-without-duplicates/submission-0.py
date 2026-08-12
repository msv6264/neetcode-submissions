class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxLen, curr = 0, 0
        l, r = 0, 0

        while r < len(s):
            dic[s[r]] = dic.get(s[r], 0) + 1

            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                l += 1

            curr = r - l + 1
            maxLen = max(maxLen, curr)

            r += 1

        return maxLen