# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        if not root:
            return None
        
        left_count = count_nodes(root.left)
        
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        elif k == left_count + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left_count - 1)