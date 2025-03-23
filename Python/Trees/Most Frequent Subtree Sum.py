#Link: https://leetcode.com/problems/most-frequent-subtree-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count_map = {}
        max_count = 0
        res = []
        def traverse(root):
            nonlocal max_count
            if not root:
                return 0
            left_tree = traverse(root.left)
            right_tree = traverse(root.right)
            curr_sum = left_tree + right_tree + root.val
            count_map[curr_sum] = count_map.get(curr_sum, 0) + 1
            max_count = max(max_count, count_map[curr_sum])
            return curr_sum

        traverse(root)
        for num, freq in count_map.items():
            if freq == max_count:
                res.append(num)
        return res
