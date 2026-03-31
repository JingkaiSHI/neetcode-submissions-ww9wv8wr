class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we don't want duplicate, so we can use a set for it
        seen = set()
        l = r = 0
        result = 0
        for char in s:
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
            result = max(result, r - l + 1)
            r += 1
        return result
        