class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern_map = {}
        current_map = {}
        matched = 0
        window_start = 0
        min_window = float('inf')
        res = [0,0]


        for el in t:
            pattern_map[el] = pattern_map.get(el,0) + 1
        

        for window_end in range(len(s)):
            current_map[s[window_end]] = current_map.get(s[window_end],0) + 1
            if current_map.get(s[window_end]) == pattern_map.get(s[window_end]):
                matched += 1

            while matched == len(pattern_map):
                
                if window_end - window_start + 1 < min_window:
                    min_window = window_end - window_start + 1
                    res = [window_start, window_end+1]

                current_map[s[window_start]] -= 1

                if s[window_start] in pattern_map and current_map[s[window_start]] < pattern_map.get(s[window_start]):
                    matched -= 1
                if current_map[s[window_start]] == 0:
                    del current_map[s[window_start]]
                window_start += 1
        return s[res[0]:res[1]]
