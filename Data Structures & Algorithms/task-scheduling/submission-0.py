class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Naturally we should think of a greedy approach by locating the most frequent task
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort() # as count is fixed length, big O is O(1)
        highest_frequency = count[25]
        idle = (highest_frequency - 1) * n

        for i in range(24, -1, -1):
            idle -= min(highest_frequency - 1, count[i])
        return max(0, idle) + len(tasks)
        