class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for ch in s:
            if len(stack) > 0 and ch in parentheses_dict:
                if parentheses_dict.get(ch) == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(ch)


        if len(stack) != 0:
            return False
        return True
        
            
