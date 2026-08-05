class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""

        if strs == []:
            return ""

        for word in strs:
            l = len(word)
            ans += str(l) + "#" + word

        return ans

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        res = []

        i = 0
        while i < len(s):
            j = i
        
            while s[j] != "#":
                j += 1
            lngth = int(s[i : j])

            res.append(s[j+1 : j + 1 + lngth])

            i = j + 1 + lngth

        return res