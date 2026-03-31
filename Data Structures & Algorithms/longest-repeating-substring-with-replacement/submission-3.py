class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest_length = 0
        max_freq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            while (r - l + 1) - max_freq > k:
                if s[l] in count:
                    count[s[l]] -= 1
                l += 1
            longest_length = max(longest_length, r - l + 1)
        return longest_length