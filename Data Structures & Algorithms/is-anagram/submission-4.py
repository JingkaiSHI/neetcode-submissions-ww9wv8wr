class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_pattern = [0] * 26
        t_pattern = [0] * 26
        for c in s:
            s_pattern[ord(c) - ord('a')] += 1
        for ch in t:
            t_pattern[ord(ch) - ord('a')] += 1
        
        return tuple(s_pattern) == tuple(t_pattern)
        