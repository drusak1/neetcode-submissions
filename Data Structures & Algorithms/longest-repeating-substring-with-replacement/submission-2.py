class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        window_start = 0
        max_len = 0
        max_freq = 0

        for window_end, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])

            while (window_end - window_start + 1) - max_freq > k:
                freq[s[window_start]] -= 1
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)

        return max_len
