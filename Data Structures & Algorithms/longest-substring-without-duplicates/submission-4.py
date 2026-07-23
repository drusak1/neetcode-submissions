class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        window_start = 0

        for window_end in range(len(s)):
            char_map[s[window_end]] = char_map.get(s[window_end], 0) + 1

            while len(char_map) < window_end - window_start + 1:
                char_map[s[window_start]] -= 1

                if char_map[s[window_start]] == 0:
                    del char_map[s[window_start]]
                
                window_start += 1

            max_len = max(max_len, window_end - window_start + 1)

        return max_len



            

            