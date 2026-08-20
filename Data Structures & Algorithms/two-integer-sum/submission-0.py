class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi={}
        for i in range(len(nums)):
            hashi[nums[i]]=i
        for j in range(len(nums)):
            diff=target-nums[j]
            if diff in hashi and hashi[diff]!=j:
                return sorted([hashi[diff],j])