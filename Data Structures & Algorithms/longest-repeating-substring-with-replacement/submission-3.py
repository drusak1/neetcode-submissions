class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        res = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_freq = max(max_freq, count[ch])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res