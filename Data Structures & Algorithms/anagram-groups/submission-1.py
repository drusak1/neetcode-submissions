# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_map =  {}

#         for string in strs:
#             s = "".join(sorted(string))
#             if hash_map.get(s) is None:
#                 hash_map[s] = []
#             hash_map[s].append(string)
#         res = []

#         for k,v in hash_map.items():
#             res.append(v)
#         return res             
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
