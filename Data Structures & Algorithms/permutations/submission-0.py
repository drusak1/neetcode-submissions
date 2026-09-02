class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def backtracing(nums,path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return


            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                path.append(nums[i])
                used.add(nums[i])

                backtracing(nums,path,used)
                path.pop()
                used.remove(nums[i])

        backtracing(nums,[], used)
        return res
    
