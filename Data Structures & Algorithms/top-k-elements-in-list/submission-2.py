from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_common_nums= [num for num, word_count in Counter(nums).most_common(k)]
        return most_common_nums