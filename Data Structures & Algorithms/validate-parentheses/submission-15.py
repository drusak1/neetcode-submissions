class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = []

        for parenthes in s:
            if parenthes in parentheses_dict:
                if len(stack) == 0:
                    return False
                if parentheses_dict.get(parenthes) != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(parenthes)

        if len(stack) > 0:
            return False
        return True