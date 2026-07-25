class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        
        for i in range(2,len(nums)):
            curr_max = max(
                nums[i] + dp[i-2],
                dp[i-1]
            )
            dp.append(curr_max)
        return max(dp[-1], dp[-2])