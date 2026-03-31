class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [[] for _ in range(n + 1)]
        result[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in result[i]:
                    for right in result[k - i - 1]:
                        result[k].append("(" + left + ")" + right)
        return result[-1]
        