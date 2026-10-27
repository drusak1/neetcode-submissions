class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        
        if not digits:
            return []

        res = []

        def backtracking(path,i):
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return

            
            

            for ch in mapping.get(digits[i]):

                path.append(ch)
                backtracking(path,i+1)
                el = path.pop()

        backtracking([],0)
        return res