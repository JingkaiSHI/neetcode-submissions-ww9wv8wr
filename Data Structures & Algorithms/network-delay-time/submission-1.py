class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]  # (time, node)

        while heap:
            time, cur = heapq.heappop(heap)

            if cur in dist:
                continue

            dist[cur] = time

            for nei, w in graph[cur]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        if len(dist) != n:
            return -1

        return max(dist.values())
        