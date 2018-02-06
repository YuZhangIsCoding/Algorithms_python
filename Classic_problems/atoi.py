class sol(object):
    def atoi(self, string):
        '''
        Need to consider all the possible inputs of strings
        '''
        i = 0
        temp = ''
        for i, item in enumerate(string):
            if (item == '-' or item == '+') and temp == '':
                temp += item
            elif item == ' ' and temp == '':
                continue
            elif item >= '0' and item <= '9':
                temp += item
            else:
                break
        sign = ['-', '+']
        if temp == '' or temp in sign:
            return 0
        elif temp[0] == '+':
            return int(temp[1:])
        return min(int(temp))

mysol = sol()
string = '    - 12'
print mysol.atoi(string)
