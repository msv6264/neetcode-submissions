class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hsh = {}

        for i in range(len(nums)):
            n = nums[i]
            hsh[n] = hsh.get(nums[i], 0) + 1
            if hsh[n] > 1:
                return True

        return False