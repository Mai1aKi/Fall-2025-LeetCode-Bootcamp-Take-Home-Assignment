class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        tmp = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    tmp.append((i, j))
        
        for r, c in tmp:
            for j in range(n):
                matrix[r][j] = 0
            for i in range(m):
                matrix[i][c] = 0

sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print("Before:", matrix)
sol.setZeroes(matrix)
print("After:", matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("Before:", matrix)
sol.setZeroes(matrix)
print("After:", matrix)

