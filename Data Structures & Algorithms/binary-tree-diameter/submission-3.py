# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        lookup = {None: (0, 0)}
        while stack:
            node = stack[-1]
            if node.left and node.left not in lookup:
                stack.append(node.left)
            elif node.right and node.right not in lookup:
                stack.append(node.right)
            else:
                # we hit a leaf
                node = stack.pop()
                leftH, leftD = lookup[node.left]
                rightH, rightD = lookup[node.right]
                lookup[node] = (max(leftH + 1, rightH + 1), max(leftH + rightH, leftD, rightD))
        return lookup[root][1]

        