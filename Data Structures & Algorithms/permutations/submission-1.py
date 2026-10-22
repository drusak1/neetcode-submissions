class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def backtracing(nums,path,used):
            if len(nums) == len(path):
                res.append(path[:])

            
            for num in nums:
                if num in used:
                    continue

                used.add(num)
                path.append(num)
                backtracing(nums,path,used)

                el = path.pop()
                used.remove(el)
        
        backtracing(nums,[],used)
        return res
