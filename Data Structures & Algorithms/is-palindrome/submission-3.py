import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = s.translate(str.maketrans('', '', string.punctuation))
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True