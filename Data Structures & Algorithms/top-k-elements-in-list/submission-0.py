class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force

        hsh = defaultdict(int)

        for num in nums:
            hsh[num] += 1

        new = sorted(hsh.items(), key = lambda x:x[1], reverse = True)

        return [num for num, freq in new[:k]]