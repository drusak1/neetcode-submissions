class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = []
        for char in s:
            if char.isalpha() or char.isdigit():
                new_s.append(char)
        new_s = "".join(new_s)

        left, right = 0, len(new_s) - 1

        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        return True