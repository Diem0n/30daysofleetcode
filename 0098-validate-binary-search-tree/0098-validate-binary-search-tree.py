# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev_val = float("-inf")

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= prev_val:
                return False
            prev_val = root.val

            root = root.right

        return True