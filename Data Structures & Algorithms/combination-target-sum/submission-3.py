class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(path,remaining,start):
            if remaining == 0:
                res.append(path[:])
                return 
            if remaining < 0:
                return

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtracking(path,remaining-nums[i],i)
                path.pop()
            

        backtracking([],target,0)
        return res