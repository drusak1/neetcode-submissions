class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(re.findall(r'[A-Za-z0-9]', s.lower()))
        left_pointer, right_pointer = 0, len(alphanumeric) - 1

        while left_pointer < right_pointer:
            if alphanumeric[left_pointer] != alphanumeric[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True