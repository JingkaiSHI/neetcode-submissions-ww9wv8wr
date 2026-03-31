class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given edges, establishing a adj list seems to be a good choice
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # graph is created, traverse it with a visited
        visited = set()
        todo = deque([(0, -1)])
        visited.add(0)
        while todo:
            cur, parent = todo.popleft()
            for neighbor in adj[cur]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                else:
                    visited.add(neighbor)
                    todo.append((neighbor, cur))
        return len(visited) == n