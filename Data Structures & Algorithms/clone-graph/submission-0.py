"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # at a certain node, we want to create a node, and properly create its neighbors
        # neighbors will be either empty array or a list of Node
        if not node:
            return None
        newNodes = {}
        def cloneNode(root):
            current = Node(root.val)
            newNodes[root.val] = current
            for neighbor in root.neighbors:
                # for each neighbor, check if already cloned
                if neighbor.val not in newNodes:
                    curNeighbor = cloneNode(neighbor)
                current.neighbors.append(newNodes[neighbor.val])
            return current

        return cloneNode(node)
        