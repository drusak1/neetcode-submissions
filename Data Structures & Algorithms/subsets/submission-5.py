class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(nums,start,res):
            result.append(res[:])
            for i in range(start, len(nums)):
                res.append(nums[i])
                backtracking(nums,i+1,res)
                res.pop()
        backtracking(nums,0,[])
        return result