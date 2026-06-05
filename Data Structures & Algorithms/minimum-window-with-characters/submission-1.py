class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmp_char_dict = {}
        t_char_dict = {}
        matches = 0
        window_start = 0
        min_window = float('inf')
        res = ""
        for i in t:
            t_char_dict[i] = t_char_dict.get(i,0) + 1

        for window_end in range(len(s)):
            tmp_char_dict[s[window_end]] = tmp_char_dict.get(s[window_end],0) + 1

            if tmp_char_dict[s[window_end]] == t_char_dict.get(s[window_end]):
                matches += 1

            while matches == len(t_char_dict):
                if window_end - window_start + 1 < min_window:
                    min_window = window_end - window_start + 1
                    res = s[window_start:window_end+1]
                
                char_at_start = s[window_start]
                if char_at_start in t_char_dict and tmp_char_dict[char_at_start] == t_char_dict[char_at_start]:
                    matches -= 1
                tmp_char_dict[char_at_start] -= 1
                window_start += 1

        return res