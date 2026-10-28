class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_polindorm(string):
            return string == string[::-1]

        res = []

        def backtracing(path,start):
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start, len(s)):
                if is_polindorm(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtracing(path,i+1)
                    path.pop()

    
        backtracing([],0)
        return res