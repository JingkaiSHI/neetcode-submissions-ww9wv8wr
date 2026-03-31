import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if len(target) <= 1:
            return True

        i = 0
        j = len(target) - 1

        while i < j:
            if target[i] != target[j]:
                return False
            i += 1
            j -= 1
        return True
        