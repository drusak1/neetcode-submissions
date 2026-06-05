from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, num_count in Counter(nums).most_common(k)]

