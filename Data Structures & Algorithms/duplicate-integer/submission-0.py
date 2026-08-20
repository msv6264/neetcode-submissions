class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        hashi={}
        for i in range(n):
            hashi[nums[i]]=hashi.get(nums[i],0)+1
            if hashi[nums[i]]>1:
                return True
        return False
