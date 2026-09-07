class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtracing(path, open, close):
            if open == n and close == n:
                res.append("".join(path[:]))
                return 

            for el in ["(", ")"]:
                if open > n or close > open:
                    continue

                
                if el == "(":
                    path.append(el)
                    backtracing(path,open+1,close)
                    path.pop()
                
                else:
                    path.append(el)
                    backtracing(path,open,close+1)
                    path.pop()
                

        backtracing([],0,0)

        return res