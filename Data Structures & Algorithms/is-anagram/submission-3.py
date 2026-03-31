class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_arr = [c for c in s]
        # t_arr = [c for c in t]
        # s_arr.sort()
        # t_arr.sort()
        # return s_arr == t_arr
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0)
        
        for char in t:
            t_dict[char] = s_dict.get(char, 0)
        
        for char in s:
            s_dict[char] += 1
        
        for char in t:
            t_dict[char] += 1
        return s_dict == t_dict
        
        