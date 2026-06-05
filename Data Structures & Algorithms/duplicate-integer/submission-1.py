from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = Counter(nums)
        for k,v in hash_map.items():
            if v > 1:
                return True
        return False