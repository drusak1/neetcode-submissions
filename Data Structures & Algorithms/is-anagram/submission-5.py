from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)
        
        for k,v in counter_s.items():
            if counter_t.get(k) != v:
                return False
        return True