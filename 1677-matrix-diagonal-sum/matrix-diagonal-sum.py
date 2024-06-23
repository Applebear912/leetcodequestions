class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i] + mat[i][n-i-1]

        if n % 2:
            middle = n//2
            sum -= mat[middle][middle]
        return sum