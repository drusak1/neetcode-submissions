from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for k,v in s_counter.items():
            if t_counter.get(k) != v:
                return False
        return True
