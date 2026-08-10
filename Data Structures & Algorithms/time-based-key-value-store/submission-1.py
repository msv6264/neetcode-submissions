class TimeMap:

    def __init__(self):
        self.hsh = {}

    def set(self, key: str, val: str, tStmp: int) -> None:
        if key not in self.hsh:
            self.hsh[key] = []

        self.hsh[key].append([val, tStmp])

    def get(self, key: str, tStmp: int) -> str:
        if key not in self.hsh:
            return ""

        l, r = 0, len(self.hsh[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if self.hsh[key][mid][1] <= tStmp:
                res = self.hsh[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res