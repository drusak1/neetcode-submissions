class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracing(nums, remaining, curr_res, start):
            if remaining == 0:
                res.append(curr_res[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                curr_res.append(nums[i])
                remaining -= nums[i]
                backtracing(nums, remaining, curr_res, i)
                remaining += nums[i]
                curr_res.pop()
        
        backtracing(nums,target,[], 0)
        return res