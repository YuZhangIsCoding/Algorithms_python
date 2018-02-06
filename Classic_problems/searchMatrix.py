class sol(object):
    def searchMatrix(self, matrix, target):
        '''
        Search the target value in an m*n matrix.
        The integers in each row are sorted from left to right
        The first integer is larger than the last integer of previous row.

        Use global binary search.
        66 ms, 12.73%.
        Second try
        52 ms, 32.10%.
        '''
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1
        while low <= high: 
            mid = (low+high)/2
            realmid = (mid/n, mid%n)
            if matrix[realmid[0]][realmid[1]] == target:
                return True
            elif matrix[realmid[0]][realmid[1]] > target:
                high = mid-1
            else:
                low = mid+1
        return False
    def searchMatrix_2(self, matrix, target):
        '''
        First locates row and then locates column. This method also avoids overflow.
        However, the performance is even worse
        69 ms, 9.04%.
        Tried second time
        42 ms, 80.07%
        '''
        if not matrix or not matrix[0]:
            return False
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = (low+high)/2
            if target < matrix[mid][0]:
                high = mid -1
            elif target > matrix[mid][-1]:
                low = mid+1
            else:
                low = 0
                high = len(matrix[mid])
                while low <= high:
                    submid = (low+high)/2
                    if matrix[mid][submid] == target:
                        return True
                    elif matrix[mid][submid] > target:
                        high = submid-1
                    else:
                        low = submid+1
                return False
        return False

    def searchWord(self, board, word):
        '''
        Given a 2D board and a word, find if the word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cell, 
        where "adjacent" cells are those horizontally or vertically neighboring. 
        Same letter cell may not be used more than once.

        The following script works fine for board and word with less duplicates,
        but achieves time limit when the board consists of a lot of duplicates.
        The use of dictionary increase the randomness of searching pattern.
        The critical step maybe the search in path.
        '''
        if len(word) < 1:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.check_nb(board, (i, j), word, 0, [(i, j)]):
                        return True
        return False

    def check_nb(self, board, coord, word, ind, path):
        if ind == len(word)-1:
            return True
        nb = self.get_nb(board, coord, path)
        for item in nb.keys():
            if word[ind+1] == nb[item]:
#                path[item] = True
                if self.check_nb(board, item, word, ind+1, path+[item]):
                    return True
        return False

    def get_nb(self, board, coord, path):
        ans = {}
        locs = [(coord[0]+1, coord[1]), (coord[0], coord[1]+1), \
                (coord[0]-1, coord[1]), (coord[0], coord[1]-1)]
        for item in locs:
#            if not path.get(item, False) and  min(item) >= 0 and item[0] < len(board)\
#                    and item[1] < len(board[0]):
            if item not in path and min(item) >= 0 and item[0] < len(board)\
                    and item[1] < len(board[0]):
                ans[item] = board[item[0]][item[1]]
        return ans

    def searchWord_2(self, board, word):
        '''
        Try to check in one direction
        This script breaks the string into lists and put '#'in the list
        if a match is found.
        '''
        if not board:
            return False
        board = [[i for i in item] for item in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check_exist(board, i, j, word, 0):
                    return True
        return False

    def check_exist(self, board, i, j, word, ind):
        if ind == len(word):
            return True
        if min(i, j) < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[ind]:
            return False
        temp = word[ind]
        board[i][j] = '#'
## the if loop is equavalent
#        if self.check_exist(board, i+1, j, word, ind+1) or\
#                self.check_exist(board, i, j+1, word, ind+1) or\
#                self.check_exist(board, i-1, j, word, ind+1) or\
#                self.check_exist(board, i, j-1, word, ind+1):
#            return True
        res = self.check_exist(board, i+1, j, word, ind+1) or\
                self.check_exist(board, i, j+1, word, ind+1) or\
                self.check_exist(board, i-1, j, word, ind+1) or\
                self.check_exist(board, i, j-1, word, ind+1)
        board[i][j] = temp
        return res


mysol = sol()
#matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
#matrix = [[]]
#target = 3
#print mysol.searchMatrix_2(matrix, target)
board = ["ABCE","SFCS","ADEE"]
board = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]

word = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print mysol.searchWord(board, word)
print mysol.searchWord_2(board, word)
