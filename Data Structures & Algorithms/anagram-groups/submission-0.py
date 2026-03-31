class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []

        for word in strs:
            key = ''.join(sorted(word))

            if key not in anagrams:
                anagrams[key] = []
            
            anagrams[key].append(word)
        return list(anagrams.values())
        