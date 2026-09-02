class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtracing(nums, remaining, curr_res, start):
            if remaining == 0:
                res.append(curr_res[:])
                return
            if remaining < 0:
                return

                
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr_res.append(nums[i])
                remaining -= nums[i]
                backtracing(nums, remaining, curr_res, i+1)
                remaining += nums[i]
                curr_res.pop()
        
        backtracing(candidates,target,[], 0)
        return res