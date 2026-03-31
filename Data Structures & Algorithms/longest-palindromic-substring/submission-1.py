class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            l, r = 0, 0
            p = [0] * n
            for i in range(n):
                p[i] = min(r - i, p[l + r - i]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l = i - p[i]
                    r = i + p[i]
            return p
        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIndex = (center_idx - resLen) // 2
        return s[resIndex: resIndex + resLen]

        