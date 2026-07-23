class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern_map = {}
        current_map = {}

        for s in s1:
            pattern_map[s] = pattern_map.get(s,0) + 1
        

        window_start = 0

        for window_end in range(len(s2)):
            current_map[s2[window_end]] = current_map.get(s2[window_end],0) + 1
            while (window_end - window_start + 1) > len(s1):
                current_map[s2[window_start]] -= 1
                
                if current_map[s2[window_start]] == 0:
                    del current_map[s2[window_start]]
                window_start += 1
            if current_map == pattern_map:
                return True
        
        return False
