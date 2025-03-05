#Link: https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        def maxSubTree(node):
            nonlocal res
            if node >= n:
                return 0
            
            left_sub_tree = maxSubTree(2 * node + 1)
            right_sub_tree = maxSubTree(2 * node + 2)

            res += abs(left_sub_tree - right_sub_tree)
            return max(left_sub_tree, right_sub_tree) + cost[node]
        maxSubTree(0)
        return res