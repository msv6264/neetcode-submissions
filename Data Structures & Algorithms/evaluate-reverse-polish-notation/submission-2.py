class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for c in tokens:
            if c not in "+-*/":
                stk.append(int(c))
            else:
                b = int(stk.pop())
                a = int(stk.pop())

                if c == '+':
                    stk.append(a + b)
                elif c == '-':
                    stk.append(a - b)
                elif c == '*':
                    stk.append(a * b)
                else:
                    stk.append(a / b)

        return int(stk[-1])
                