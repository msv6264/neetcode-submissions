class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}

        for c1 in s:
            dic[c1] = dic.get(c1, 0) + 1

        for c2 in t:
            if c2 not in dic:
                return False

            dic[c2] -= 1

            if dic[c2] < 0:
                return False

        return True