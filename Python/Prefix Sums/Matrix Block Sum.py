#Link: https://leetcode.com/problems/matrix-block-sum/
class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        prefix_sum = [ [0] * (len(matrix[0])+1) for _ in range(len(matrix)+1) ]
        
        def calculate_prefix_sum():
            for i in range(1, len(matrix)+1):
                for j in range(1, len(matrix[0])+1):
                    prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        
        calculate_prefix_sum()
        ans = [ [0] * (len(matrix[0])) for _ in range(len(matrix)) ]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r1, c1 = max(0, i-k), max(0, j-k)
                r2, c2 = min(len(matrix)-1, i+k), min(len(matrix[0]) - 1, j+k)
                ans[i][j] = prefix_sum[r2+1][c2+1] - prefix_sum[r2+1][c1] - prefix_sum[r1][c2+1] + prefix_sum[r1][c1]
        return ans