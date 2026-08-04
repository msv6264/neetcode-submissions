class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            b = target - nums[i]

            if b in dic:
                return [dic[b], i]

            dic[nums[i]] = i