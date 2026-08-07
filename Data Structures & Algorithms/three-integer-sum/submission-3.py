class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        res = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            lft, rght = i + 1, n - 1

            while lft < rght:
                tot = arr[lft] + arr[rght] + arr[i]

                if tot < 0:
                    lft += 1

                elif tot > 0:
                    rght -= 1

                else:
                    res.append([arr[lft], arr[rght], arr[i]])

                    lft += 1
                    rght -= 1

                    while lft < rght and arr[lft] == arr[lft - 1]:
                        lft += 1

                    while lft < rght and arr[rght] == arr[rght + 1]:
                        rght -= 1

        return res