class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_char = {}
        window_start = 0
        tmp_dir_char = {}

        if len(s2) < len(s1):
            return False

        for s in s1:
            dict_char[s] = dict_char.get(s,0) + 1

        for i in range(len(s2)):
            if i >= len(s1):
                tmp_dir_char[s2[i-len(s1)]] -= 1
                if tmp_dir_char[s2[i-len(s1)]] == 0:
                    del tmp_dir_char[s2[i-len(s1)]]
            tmp_dir_char[s2[i]] = tmp_dir_char.get(s2[i],0) + 1

            if tmp_dir_char == dict_char:
                return True
        return False


        
        
