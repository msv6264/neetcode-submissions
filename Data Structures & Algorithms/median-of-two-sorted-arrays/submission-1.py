class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        
        if i <= len(nums1):
            arr += nums1[i:]

        if j <= len(nums2):
            arr += nums2[j:]

        n = len(arr)

        if n % 2 == 0:
            mid = n // 2
            return (arr[mid] + arr[mid - 1]) / 2
        else:
            mid = n // 2
            return arr[mid]