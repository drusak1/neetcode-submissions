class Solution:
    def check(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            prev, curr = curr, max(curr, prev + n)
        return curr
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        ans_1 = self.check(nums[1:])
        ans_2 = self.check(nums[:-1])
        return max(ans_1, ans_2)