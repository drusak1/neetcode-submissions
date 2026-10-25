class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracing(path,start):
            if len(path) == k:
                res.append(path[:])
                return
            if len(path) > k:
                return
            
            for i in range(start,n+1):
                path.append(i)
                backtracing(path,i+1)
                path.pop()
        backtracing([],1)
        return res