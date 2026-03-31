class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        pattern = {}
        window = {}
        for c in t:
            pattern[c] = pattern.get(c, 0) + 1
        
        have, need = 0, len(pattern)
        result, result_length = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in pattern and window[c] == pattern[c]:
                have += 1
            while have == need:
                if (r - l + 1) < result_length:
                    result = [l, r]
                    result_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in pattern and window[s[l]] < pattern[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l:r + 1] if result_length != float("infinity") else ""

        