class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n log n time comp, > than hashtable and set solutions
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False