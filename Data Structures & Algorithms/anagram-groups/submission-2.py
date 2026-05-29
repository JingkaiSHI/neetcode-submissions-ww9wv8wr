class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a dictionary, or hashmap
        patterns = {}
        # key would be tuple pattern of characters, since we only have lowercase english letter, we can do this
        # value would be the words
        for word in strs:
            # pattern as a list of 0 (length of 26)
            pattern = [0] * 26
            for char in word:
                i = ord('a') - ord(char)
                pattern[i] += 1
            # look at the dictionary, is the pattern there?
            if tuple(pattern) in patterns:
                patterns[tuple(pattern)].append(word)
            else:
                patterns[tuple(pattern)] = [word]
        
        # we just need to return the values of the dictionary
        return list(patterns.values())
        