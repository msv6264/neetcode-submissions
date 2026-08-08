class Solution:
    def dailyTemperatures(self, tmp: List[int]) -> List[int]:
        stk = []
        n = len(tmp)
        res = [0] * n

        for i in range(n):
            while stk and tmp[stk[-1]] < tmp[i]:
                idx = stk.pop()
                res[idx] = i - idx

            stk.append(i) 
        return res