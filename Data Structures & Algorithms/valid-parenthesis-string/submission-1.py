class Solution:
    def checkValidString(self, s: str) -> bool:
        # it is valid parenthesis but added a wild card character
        # we go through the string
        # we need to keep track of 2 variables
        # - stack: to keep track of (
        # - free: int to keep track of * we have seen
        left = []
        free = []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                free.append(i)
            else:
                if not left and not free:
                    return False
                if left:
                    left.pop()
                else:
                    free.pop()
        while left and free:
            if left.pop() > free.pop():
                return False

        return not left
        