class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        pattern = {}
        for a in s1:
            pattern[a] = pattern.get(a, 0) + 1
        
        l = 0
        cur_pattern = {}
        for r in range(len(s2)):
            cur_pattern[s2[r]] = cur_pattern.get(s2[r], 0) + 1
            if (r - l + 1) > len(s1):
                cur_pattern[s2[l]] -= 1
                if cur_pattern[s2[l]] == 0:
                    del cur_pattern[s2[l]]
                l += 1
            if cur_pattern == pattern:
                return True

        return False
        