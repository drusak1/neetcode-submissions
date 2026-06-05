class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        lst = []

        if len(s) <= 1:
            return False

        for par in s:
            if par in ["{", "(", "["]:
                lst.append(par)
            elif par in par_dict and (len(lst) == 0 or par_dict[par] != lst[-1]):
                return False
            else:
                lst.pop()
        
        if len(lst) == 0:
            return True
        else:
            return False