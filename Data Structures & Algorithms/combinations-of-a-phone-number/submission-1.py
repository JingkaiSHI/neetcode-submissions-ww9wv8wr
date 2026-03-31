class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        path = []
        lookup = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": ["+"]
        }

        def backtrack(i):
            if i == len(digits):
                if len(path) == 0:
                    return
                cur = "".join(path)
                result.append(cur)
                return
            for char in lookup[digits[i]]:
                path.append(char)
                backtrack(i + 1)
                path.pop()
            return 
        backtrack(0)
        return result