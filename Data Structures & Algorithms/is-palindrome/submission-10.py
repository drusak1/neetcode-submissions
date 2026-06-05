class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:
            while not s[left_pointer].isalnum() and left_pointer < right_pointer:
                left_pointer += 1
            while not s[right_pointer].isalnum() and left_pointer < right_pointer:
                right_pointer -= 1

            if  s[left_pointer].isalnum() and \
                s[right_pointer].isalnum() and \
                s[left_pointer] != s[right_pointer]:
                return False

            left_pointer += 1
            right_pointer -= 1
        return True        