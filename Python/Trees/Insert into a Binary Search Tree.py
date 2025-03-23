#Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(root): 
            if val < root.val:
                if root.left:
                    traverse(root.left)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    traverse(root.right)
                else:
                    root.right = TreeNode(val)
        if not root:
            root = TreeNode(val)
            return root
        traverse(root)
        return root