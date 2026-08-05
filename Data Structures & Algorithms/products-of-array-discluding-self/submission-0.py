class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        res = []
        for i in range(len(nums)):
            mul = 1

            for j in range(len(nums)):
                if j != i:
                    mul *= nums[j]

            res.append(mul)

        return res