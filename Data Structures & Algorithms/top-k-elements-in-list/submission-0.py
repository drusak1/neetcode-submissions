from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = Counter(nums)
        res = []
        for kv in counter_map.most_common(k):
            res.append(kv[0])
        return res
        