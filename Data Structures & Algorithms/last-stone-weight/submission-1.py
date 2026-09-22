class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_max = [-stone for stone in stones]
        heapq.heapify(stones_max)

        while len(stones_max) >= 2:
            max_el = heapq.heappop(stones_max)
            second_max_el = heapq.heappop(stones_max)

            if max_el != second_max_el:
                heapq.heappush(stones_max, max_el-second_max_el)
        
        if len(stones_max) == 1:
            return -stones_max[0]
        return 0


