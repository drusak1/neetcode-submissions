class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracing(path, ind):
            res.append(path[:])
            for i in range(ind,len(nums)):
                
                path.append(nums[i])
                backtracing(path,i+1)
                path.pop()

        
        backtracing([],0)
        return res
            