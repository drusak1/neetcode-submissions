class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(path,remaining,start):
            if remaining == 0:
                res.append(path[:])
                return 

            for i in range(start,len(nums)):
                if nums[i] > remaining:
                    break
                path.append(nums[i])
                backtracking(path,remaining-nums[i],i)
                path.pop()
            

        backtracking([],target,0)
        return res