class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    prev = stack.pop()
                    if char == ")" and prev == "(":
                        continue
                    elif char == "]" and prev == "[":
                        continue
                    elif char == "}" and prev == "{":
                        continue
                    else:
                        return False
        return len(stack) == 0
        