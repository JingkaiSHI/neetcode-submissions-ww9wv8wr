class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            pattern = [0] * 26
            for c in word:
                pattern[ord(c) - ord('a')] += 1
            pattern = tuple(pattern)
            if pattern in groups:
                groups[pattern].append(word)
            else:
                groups[pattern] = [word]
        return list(groups.values())
        