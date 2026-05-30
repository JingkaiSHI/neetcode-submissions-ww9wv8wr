class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # natural way to do it is through 2 pointers
        ptr_t = 0
        for char in s:
            if char == t[ptr_t]:
                ptr_t += 1
            if ptr_t == len(t):
                return 0
        return len(t) - ptr_t
        