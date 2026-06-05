from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)

        for k,v in anagram_dict.items():
            res.append(v)
        return res
            
        