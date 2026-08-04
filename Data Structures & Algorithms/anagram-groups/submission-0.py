class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        ans = []
        angms = []
        sub = []

        for w in strs:
            old = w
            anagrm = tuple(sorted(w))

            if anagrm in hsh:
                hsh[anagrm].append(old)
            else:
                angms.append(anagrm)
                hsh[anagrm] = [old]

        for a in angms:
            sub = hsh[a]
            ans.append(sub)

        return ans