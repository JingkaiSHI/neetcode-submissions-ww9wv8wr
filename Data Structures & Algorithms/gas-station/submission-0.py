class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # edge case: if sum of cost is larger than sum of gas, it is impossible to finish
        if sum(gas) < sum(cost):
            return -1
        
        # any index with a surplus can be a start
        total = 0
        res = 0
        n = len(cost)
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res

        