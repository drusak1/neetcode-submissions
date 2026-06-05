class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            escaped_str = s.replace("#", "##")
            encoded_str += f"#{len(escaped_str)}:{escaped_str}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                i += 1
                idx = s.find(":", i)
                length = int(s[i:idx])
                raw_str = s[idx+1:idx+1+length]
                res.append(raw_str.replace("##", "#"))
                i = idx + 1 + length
            else:
                i += 1
        return res
