class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l = 0
        r = len(target) - 1
        while l < r:
            if target[l] != target[r]:
                return False
            l += 1
            r -= 1
        return True
        