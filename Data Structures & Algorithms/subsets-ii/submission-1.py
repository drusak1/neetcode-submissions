class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        def backtracing(path,start):
            if path in res:
                return
            res.append(path[:])

            for i in range(start,len(nums)):
                
                path.append(nums[i])
                backtracing(path,i+1)
                path.pop()
        
        backtracing([],0)
        return res
