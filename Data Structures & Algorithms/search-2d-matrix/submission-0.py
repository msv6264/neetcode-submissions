class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)
        rowLen = len(mat[0])

        l, r = 0, n - 1
        row = -1

        while l <= r:
            mid = l + (r - l) // 2

            if mat[mid][0] <= target:
                row = mid
                l = mid + 1
            else:
                r = mid - 1

        if row == -1:
            return False

        def binSearch(arr, t):
            l, r = 0, len(arr) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if arr[mid] == t:
                    return mid

                elif arr[mid] < t:
                    l = mid + 1

                else:
                    r = mid - 1

            return -1

        return binSearch(mat[row], target) != -1