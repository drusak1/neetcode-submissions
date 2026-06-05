class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        s1_len = len(s1)

        char_dict_s1 = {}
        char_dict_s2 = {}

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            if char_dict_s1.get(s1[i]) is None:
                char_dict_s1[s1[i]] = 0
            char_dict_s1[s1[i]] += 1

        for window_end in range(len(s2)):
            if char_dict_s2.get(s2[window_end]) is None:
                char_dict_s2[s2[window_end]] = 0
            char_dict_s2[s2[window_end]] += 1

            while (window_end - window_start + 1) > s1_len:
                char_dict_s2[s2[window_start]] -= 1
                if char_dict_s2[s2[window_start]] == 0:
                    del char_dict_s2[s2[window_start]]
                window_start += 1

            if char_dict_s1 == char_dict_s2:
                return True
        return False

        

        
