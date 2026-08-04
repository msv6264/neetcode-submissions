class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)

        res = True if len(ans) < len(nums) else False
        return res