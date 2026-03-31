class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [(pos, s) for pos, s in zip(position, speed)]
        fleets.sort(reverse=True)
        stack = []
        for pos, s in fleets:
            stack.append((target - pos) / s)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
        