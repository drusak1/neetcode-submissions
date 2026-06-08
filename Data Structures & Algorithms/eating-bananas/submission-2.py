class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            curr_time = 0
            mid = (left+right) // 2
            for p in piles:
                curr_time += math.ceil(float(p) / mid)

            if curr_time > h:
                left = mid + 1
            else:
                right = mid
        return left
            
