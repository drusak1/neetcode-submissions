class Solution:
    def isValid(self, s: str) -> bool:
        right_chars = [")", "}", "]"]
        left_chars = ["(", "{", "["]
        
        char_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for i in s:
            if i in left_chars:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
    
                last_el = stack.pop()
                if char_map.get(last_el) != i:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
