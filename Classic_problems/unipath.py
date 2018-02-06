class Sol(object):
    def uniquePaths(self, m, n):
        '''
        Find the unique path from (1, n) to (m, 1). The idea is basically the idea of C(m+n-2)(m-1).
        '''
## time limit exceed
## Too many recursions
        if m == 1:
            return 1
        if n == 1:
            return 1
        return self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)

    def uniquePaths_2(self, m, n):
        '''
        Construct the whole list by summing up previous elements
        '''
        mylist = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mylist[i][j] = mylist[i-1][j]+mylist[i][j-1]
        return mylist[m-1][n-1]

    def uniquePaths_3(self, m, n):
        '''
        The previous function can be optimized by reducing the size of the list to 2 rows,
        since each time, we just need to use the last row for the summation. The space needed
        is reduced to O(min(m, n))
        '''
        if m > n:
            return self.uniquePaths_3(n, m)
        pre = [1]*m
        cur = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                cur[j] = cur[j-1]+pre[j]
            pre = cur[:]
        return pre[-1]
    
    def uniquePaths_4(self, m, n):
        '''
        The space can be further reduced to 1 row, we could just update the row.
        '''
        if m > n:
            return self.uniquePaths_3(n, m)
        cur = [1]*m
        for i in range(1, n):
            for j in range(1, m):
                cur[j] += cur[j-1]
        return cur[-1]
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cur = [0]*n
        j = 0
        while j < n and obstacleGrid[0][j] == 0:
            cur[j] = 1
            j += 1
        for i in range(1, m):
            cur[0] *= 1-obstacleGrid[i][0]
            for j in range(1, n):
                cur[j] = (1-obstacleGrid[i][j])*(cur[j]+cur[j-1])
        return cur[-1]

    def uniquePathsWithObstacles_2(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mylist = [[0]*n for i in range(m)]  
        j = 0
        while j < n and obstacleGrid[0][j] == 0: 
            mylist[0][j] = 1
            j += 1
        j = 0
        while j < m and obstacleGrid[j][0] == 0:
            mylist[j][0] = 1
            j += 1
        for i in range(1, m):
            for j in range(1, n):
                mylist[i][j] = (1-obstacleGrid[i][j])*(mylist[i-1][j]+mylist[i][j-1])
        return mylist[-1][-1]

    def uniquePathsWithObstacles_3(self, obstacleGrid):
        '''
        Can just modify obstacleGrid to store the results
        '''
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]+obstacleGrid[i-1][j]
        return obstacleGrid[-1][-1]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        cur = [sum(grid[0][:i]) for i in range(1, n+1)]
        for i in range(1, m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], cur[j])+grid[i][j]
        return cur[-1]

mysol = Sol()
m = 12
n = 23
#print mysol.uniquePaths(m, n)
#print mysol.uniquePaths_2(m, n)
#print mysol.uniquePaths_3(m, n)
#from math import factorial
#print factorial(m+n-2)/factorial(m-1)/factorial(n-1)

#mat = [[0,0,1,0,0], [1,0, 0, 0, 0]]
#mat = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0]]
#print mysol.uniquePathsWithObstacles(mat)
#print mysol.uniquePathsWithObstacles_2(mat)
#print mysol.uniquePathsWithObstacles_3(mat)

import random
mat = [[random.randint(0, 5) for j in range(4)] for i in range(4)]
print mat
print mysol.minPathSum(mat)
