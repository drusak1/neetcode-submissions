from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        for k,v in cnt_s.items():
            if v != cnt_t.get(k):
                return False
        return True
