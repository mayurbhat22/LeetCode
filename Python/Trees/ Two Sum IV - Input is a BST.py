#Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        count_map = set()

        def traverse(root):
            if not root:
                return False

            if k - root.val in count_map:
                return True
            count_map.add(root.val)
            return traverse(root.left) or traverse(root.right)
        return traverse(root)