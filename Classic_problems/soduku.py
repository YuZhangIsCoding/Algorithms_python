class sol(object):
    def isValidSudoku(self, board):
        '''
        Only the filled cells need to be validated.

        The following scripts treats the board consist of 9 cells.
        '''
        for i in range(3):
            for j in range(3):
                if self.check_duplicates(board[3*i+j]):
                    return False
                row = []
                col = []
                for k in range(3):
                    for m in range(3):
                        row.append(board[3*i+k][3*j+m])
                        col.append(board[3*k+i][3*m+j])
                for item in [row, col]:
                    if self.check_duplicates(item):
                        return False
        return True
    def check_duplicates(self, vals):
        n = len(vals)
        for i in range(n):
            if vals[i] == '.':
                continue
            for j in range(i+1, n):
                if vals[i] == vals[j]:
                    return True
        return False

    def isValidSudoku_2(self, board):
        '''
        The idea is to check case by case. Check all the rows and columns and 
        sub-cells if they contain duplicates.

        135 ms, 12.5%
        Put the first 2 if statement first improves to 92 ms, 45%
        '''
        grid = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                grid[i/3*3+j/3].append(board[i][j])
## The following code can be simplied into just 2 loop above
#        for i in range(3):
#            for j in range(3):
#                for k in range(3):
#                    for m in range(3):
#                        grid[3*i+k].append(board[3*i+j][3*k+m])
        for sub in [board, zip(*board), grid]:
            for item in sub:
                if self.check_duplicates(item):
                    return False
        return True
    
    def isValidSudoku_3(self, board):
        '''
        The method above may double check some numbers in some cases. This could be
        imporved by introducing extra memory to store whether a number already
        exist in current row, col and grid.

        76 ms, 77.8%
        '''
        mydict = {}
        col = [[0]*9 for _ in range(9)]
        grid = [[0]*9 for _ in range(9)]
        for i in range(9):
            row = [0]*9
            for j in range(9):
                if board[i][j] == '.':
                    continue
## Using dictionary seems to improve the speed
#                num = ord(board[i][j])-ord('1')
## Or we could use int to convert the string into int
#               num = int(board[i][j])-1
                num = mydict.get(board[i][j], int(board[i][j])-1)
                if row[num] or col[j][num] or grid[i/3*3+j/3][num]:
                    return False
                row[num] = col[j][num] = grid[i/3*3+j/3][num] = 1 
        return True

    def isValidSudoku_4(self, board):
        '''
        Using sets to check duplicates!

        65 ms, 95.14%
        '''
        seen = []
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item != '.':
                    ## Here to use (i, item) and (item, j) to avoid duplicates
                    seen += (i, item),(item, j), (i/3, j/3, item)
        return len(seen) == len(set(seen))

    def solveSudoku(self, board):
        '''
        Assume there will be only one unique solution
        '''
        return

mysol = sol()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
import numpy as np
print np.array([[i for i in item] for item in board])
#print mysol.isValidSudoku_4(board)
mysol.solveSudoku(board)
print np.array([[i for i in item] for item in board])
