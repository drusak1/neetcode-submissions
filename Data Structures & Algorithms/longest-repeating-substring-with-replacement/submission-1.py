class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        window_start = 0
        max_len = 0 

        for window_end in range(len(s)):
            freq[s[window_end]] = freq.get(s[window_end], 0) + 1
            max_freq = max(freq.values())
            while  window_end - window_start + 1 - max_freq > k:
                freq[s[window_start]] -= 1
                if  freq[s[window_start]] == 0:
                    del freq[s[window_start]]
                max_freq = max(freq.values())
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len