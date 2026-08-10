class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)

        if not n % 2:
            mid = n // 2
            return (arr[mid] + arr[mid - 1]) / 2
        else:
            mid = n // 2
            return arr[mid]