# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 1
        todo = []
        todo.append((root, max_depth))
        while len(todo) > 0:
            cur_node, cur_depth = todo.pop(0)
            if not cur_node.left and not cur_node.right:
                # this is a leaf node
                if cur_depth >= max_depth:
                    max_depth = cur_depth
            if cur_node.left:
                todo.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                todo.append((cur_node.right, cur_depth + 1))
        return max_depth
        