from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = Counter(s)
        t_map = Counter(t)

        for char in s:
            if s_map.get(char) != t_map.get(char):
                return False
        return True