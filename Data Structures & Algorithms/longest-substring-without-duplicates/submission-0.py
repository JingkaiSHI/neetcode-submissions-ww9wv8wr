class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the ideal time/space complexity for this problem is O(n) and O(m)
        # from this information, we can infer that no iteration inside a loop
        # we need to apply a sliding window, shrinking window size accordingly
        # we need to find a way to check duplicate in constant time
        # this clue indicates a usage of corresponding set for the sliding window
        l = 0
        longest_string_length = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            # as we synced the char set with the window, r - l = len(char_set)
            longest_string_length = max(longest_string_length, len(char_set))
        return longest_string_length
        