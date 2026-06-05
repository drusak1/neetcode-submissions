import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for num,appear in count.items():
            heapq.heappush(heap, (appear, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        