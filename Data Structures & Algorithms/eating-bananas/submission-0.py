from math import ceil

class Solution:
    # here we are using bin search, coz see, we need to check if each number can be k
    # so for that min would be obviously 1 and max will max(piles)
    # and there comes a trick now,, we know the bound of where the answer will be
    # so we need to linearly check if each num can become k
    # then why check linearly ?? use binary seach 
    # SO, WHENEVER YOU KNOW BOUND OF ANS, YOU CAN USE BINARY SEARCH

    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        if hours == len(piles):
            return max(piles)

        def canEat(k):
            hrs = sum(ceil(pile / k) for pile in piles)
            return hrs <= hours

        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2

            if canEat(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l