class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]


            max_sum = max(max_sum,curr)
        return max_sum