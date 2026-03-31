from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        todo = deque()
        todo.append(root)
        while len(todo) > 0:
            cur_node = todo.popleft()
            tmp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = tmp
            if cur_node.left:
                todo.append(cur_node.left)
            if cur_node.right:
                todo.append(cur_node.right)

        return root

        