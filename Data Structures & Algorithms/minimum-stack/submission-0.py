class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk:
            return self.stk.pop()
        return None

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        return None

    def getMin(self) -> int:
        return min(self.stk)