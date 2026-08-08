class Solution:
    def carFleet(self, trgt: int, pos: List[int], s: List[int]) -> int:
        cars = list(zip(pos, s))
        cars.sort(reverse=True)

        fleets, lstTime = 0, 0

        for pos, speed in cars:
            time = (trgt - pos) / speed

            if time > lstTime:
                fleets += 1
                lstTime = time

        return fleets