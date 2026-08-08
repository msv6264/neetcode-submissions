class Solution:
    def search(self, arr: List[int], t: int) -> int:
        n = len(arr) - 1
        l, r = 0, n

        while l <= r:
            mid = l + ((r - l) // 2)

            if arr[mid] == t:
                return mid

            elif arr[mid] < t:
                l = mid + 1
            
            else:
                r = mid - 1

        return -1