class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        max_len = 0
        window_start = 0

        max_repeat_char = 0

        for window_end in range(len(s)):
            if char_dict.get(s[window_end]) is None:
                char_dict[s[window_end]] = 0
            char_dict[s[window_end]] += 1
            
            max_repeat_char = max(max_repeat_char, char_dict[s[window_end]])


            while window_end - window_start + 1 - max_repeat_char > k:
                char_dict[s[window_start]] -= 1
                if char_dict[s[window_start]] == 0:
                    del char_dict[s[window_start]]
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)

        return max_len