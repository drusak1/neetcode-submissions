class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracing(path,start):
            res.append(path[:])

            for i in range(start,len(nums)):

                path.append(nums[i])
                backtracing(path,i+1)
                path.pop()
            
        backtracing([],0)
        return res