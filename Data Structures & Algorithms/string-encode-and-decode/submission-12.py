class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        res = []
        start_i = 0
        i = 0
        while i < len(s):
            if s[i] == "#":
                num = int(s[start_i:i])
                word = s[i+1:i+1+num]
                res.append(word)
                i = i + 1 + num
                start_i = i
            else:
                i += 1
        return res