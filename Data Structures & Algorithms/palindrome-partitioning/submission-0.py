class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def backtrack(i):
            if i == len(s):
                result.append(path.copy())
                return
            for j in range(i, len(s)):
                isPalindrome = True
                l = i
                r = j
                while l < r:
                    if s[l] != s[r]:
                        isPalindrome = False
                    l += 1
                    r -= 1
                
                if isPalindrome:
                    path.append(s[i:j + 1])
                    backtrack(j + 1)
                    path.pop()
        backtrack(0)
        return result
        