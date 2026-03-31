class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        pattern = [0] * 26
        s1_p = [0] * 26
        for c in s1:
            s1_p[ord(c) - ord('a')] += 1
        
        s1_pattern = tuple(s1_p)
        l = 0
        for r in range(len(s2)):
            pattern[ord(s2[r]) - ord('a')] += 1
            if sum(pattern) > len(s1):
                pattern[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if tuple(pattern) == s1_pattern:
                return True
            
        return False 
        