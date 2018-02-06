class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        count = 0
        while n > 1:
            for i in range(n-1):
                matrix[count+i][count], matrix[~count][count+i], matrix[~(count+i)][~count],\
                        matrix[count][~(count+i)] = matrix[~count][count+i], \
                        matrix[~(count+i)][~count], matrix[count][~(count+i)],\
                        matrix[count+i][count]
            n -= 2
            count += 1
        return 

    def spiralOrder(self, matrix):
        '''
        given a matrix of m*n elements, return all elements of the matrix in spiral order
        '''
        if matrix == []:
            return []
        elif matrix[0] == []:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            return [i[0] for i in matrix]
        return matrix[0]+[i[-1] for i in matrix[1:-1]]+matrix[-1][::-1]+\
                [i[0] for i in matrix[1:-1][::-1]]+\
                self.spiralOrder([i[1:-1] for i in matrix[1:-1]])
    def spiralOrder_2(self, matrix):
        '''
        This function just use rotate anticlockwisely
        '''
        return matrix and list(matrix.pop(0)) + self.spiralOrder_2(zip(*matrix)[::-1])

    def genMatrix(self, n):
        '''
        Given an integer n, generate a square matrix filled with elements from 1 to n^2
        in spiral order.
        '''
        ans = [[] for _ in range(n)]
        base = [0]
        i = n
        while i > 0:
            if i == 1:
                base.append(base[-1]+1)
            else:
                base.append(base[-1]+4*i-4)
            i -= 2
        for i in range(n):
            for j in range(n):
                loop = min(i, j, n-i-1, n-j-1)
                if i == loop and j >= loop and j <= n-loop-1:
                    temp = base[loop]+j-loop+1
                elif j == n-loop-1 and i >= loop and i <= n-loop-1:
                    temp = base[loop]+n-2*loop+i-loop
                elif i == n-loop-1 and j >= loop and j <= n-loop-1:
                    temp = base[loop]+2*n-4*loop-2+n-loop-j
                else:
                    temp = base[loop+1]-i+loop+1
                ans[i].append(temp)
        return ans
    def genMatrix_2(self, n):
        '''
        First asign each elements as 0, then modify
        '''
        ans = [[1]*n for _ in range(n)]
        loop = 0
        i, j = 0, 0
        for temp in range(1, n*n+1):
            ans[i][j] = temp
            if i == loop and j < n-loop-1:
                j += 1
            elif j == n-loop-1 and i < n-loop-1:
                i += 1
            elif i == n-loop-1 and j > loop:
                j -= 1
            elif j == loop and i > loop-1:
                i -= 1
            if i == loop+1 and j == loop:
                loop += 1
        return ans
    
    def genMatrix_3(self, n):
        '''
        The idea is to always rotate the matrix clockwisely and add a top row.
        '''
        ans = []
        bot = n*n+1
        while bot > 1:
            bot, top = bot-len(ans), bot
            ans = [range(bot, top)]+zip(*ans[::-1])
        return ans

    def genMatrix_4(self, n):
        '''
        Idea is to walk the spiral path and write the number, make a right term when
        the next cell is non-zero.
        Uses the notion of periodic boundary with mod operation.
        '''
        ans = [[0]*n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for temp in range(1, n*n+1):
            ans[i][j] = temp
            if ans[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return ans

    def setZeros(self, matrix):
        '''
        Set the entire row and column to 0, and do it in place
        First find and then modify.
        '''
        row = []
        col = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in col:
                        col.append(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for i in col:
            for j in range(m):
                matrix[j][i] = 0
        return
    def setZeros_2(self, matrix):
        '''
        '''
        return


mysol = Solution()
#import random
#import numpy as np
#mat = [[random.randint(0, 10) for _ in range(5)] for _ in range(5)]
#temp = np.rot90(mat, -1)
#mysol.rotate(mat)
#print np.array(mat)
#if temp.all() == np.array(mat).all():
#    print True

#mat = [[1,2,3, 4],[4,5,6,7],[7,8,9,10], [10,11,12,13]]
#mat = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
#mat = [range(10),range(10)]
#mat = [range(10)]
#mat = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
#print mysol.spiralOrder(mat)
#print mysol.spiralOrder_2(mat)

#import numpy as np
#print np.array(mysol.genMatrix(6))
#print np.array(mysol.genMatrix_2(6))
#print np.array(mysol.genMatrix_3(6))
#print np.array(mysol.genMatrix_4(6))

import random, numpy
mat = [[random.randint(0, 5) for i in range(5)] for j in range(5)]
print numpy.array(mat)
mysol.setZeros(mat)
print numpy.array(mat)
