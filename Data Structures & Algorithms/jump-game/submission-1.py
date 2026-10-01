class Solution:
    def canJump(self, nums: List[int]) -> bool:
             
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]

            if i == len(nums)-1 or nums[i] >= len(nums) - i:
                memo.update({i:True})
                return True

            for ind in range(1, nums[i] + 1):
                
                if helper(i + ind):
                    memo.update({i:True})
                    return True
            memo.update({i:False})
            return False

        return helper(0)