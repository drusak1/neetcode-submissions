class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        window_start = 0
        max_len = 0
        for window_end in range(len(s)):
            if char_dict.get(s[window_end]) is None:
                char_dict[s[window_end]] = 0
            char_dict[s[window_end]] += 1


            while char_dict[s[window_end]] > 1:
                char_dict[s[window_start]] -= 1
                if char_dict[s[window_start]] == 0:
                    del char_dict[s[window_start]]
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)
        return max_len
                
