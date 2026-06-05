from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = Counter(nums)

        for k,v in count_nums.items():
            if v > 1:
                return True
        return False
        