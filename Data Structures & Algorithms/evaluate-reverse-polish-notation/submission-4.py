class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for char in tokens:
            if char == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif char == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif char == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            elif char == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(float(val2) / val1))
            else:
                stack.append(int(char))
        return stack[0]
        