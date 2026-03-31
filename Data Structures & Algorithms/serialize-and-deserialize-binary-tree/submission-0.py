# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    # to do so, we need to understand how to represent a node
    # as node value is in the range of -1000 and +1000
    # we can encode a node with val x as +x or -x if x is negative
    # for example, 100 becomes +100, -1000 becomes -1000, essentially, a node's start/end is signified by the sign
    # great, we now have a way to encode a sequence of node, how to retain the sequence then? we can encode 2 sequences: preorder and inorder, we can definitely reconstruct this
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if nodes[0] == "N":
            return None
        root = TreeNode(int(nodes[0]))
        todo = deque([root])
        index = 1
        while todo:
            node = todo.popleft()
            if nodes[index] != "N":
                node.left = TreeNode(int(nodes[index]))
                todo.append(node.left)
            index += 1
            if nodes[index] != "N":
                node.right = TreeNode(int(nodes[index]))
                todo.append(node.right)
            index += 1
        return root

    
