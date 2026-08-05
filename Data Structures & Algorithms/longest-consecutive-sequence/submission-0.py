class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        mxLen = 1
        currLen = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                currLen += 1
            else:
                mxLen = max(mxLen, currLen)
                currLen = 1

        return max(mxLen, currLen)