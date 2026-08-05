class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zero_count = 0
        idx = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                idx = i
            else:
                mul *= nums[i]

        # prod = 0 if zero cnt > 2
        if zero_count >= 2:
            return [0] * len(nums)

        res = []

        for i in range(len(nums)):
            if zero_count == 1:
                if i == idx:
                    res.append(mul)
                else:
                    res.append(0)

            else:
                res.append(mul // nums[i])

        return res