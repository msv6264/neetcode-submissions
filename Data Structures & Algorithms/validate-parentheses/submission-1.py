class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hsh = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c not in hsh:
                stk.append(c)
            else:
                if stk and stk[-1] == hsh[c]:
                    stk.pop()
                else:
                    return False

        return True if not stk else False