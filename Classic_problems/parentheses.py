class sol(object):
    def generateParenthesis(self, n):
        '''
        Given n pairs of parenthesis, generate all combination of parentheses.

        The idea is to build from step to step, starting from '(', in each step
        '(' is added unless all '(' is used, pos list keeps tracking the number
        of '(' used. ')' will be add only when the number of '(' minus the number 
        of ')' is larger than 0, represented by the  variable count.

        79 ms, 15.77%
        '''
        if n == 0:
            return [""]
        ans = [['(']]
        count = [1]
        pos = [1]
        for _ in range(2*n-1):
            temp1 = []
            temp2 = []
            temp3 = []
            for i, item in enumerate(ans):
                if pos[i] < n:
                    temp1.append(item+['('])
                    temp2.append(count[i]+1)
                    temp3.append(pos[i]+1)
                if count[i] > 0:
                    temp1.append(item+[')'])
                    temp2.append(count[i]-1)
                    temp3.append(pos[i])
            ans = temp1
            count = temp2
            pos = temp3
        ans = [''.join(item) for item in ans]
        return ans
    def generateParenthesis_2(self, n):
        '''
        Same idea, but uses recursion.

        52 ms, 63.40%
        '''
        ans = []
        self.recursion(ans, '', 0, 0, n)
        return ans
    def recursion(self, ans, string, left, right, n):
        if len(string) == 2*n:
            ans.append(string)
            return
        if left < n:
            self.recursion(ans, string+'(', left+1, right, n)
        if right < left:
            self.recursion(ans, string+')', left, right+1, n)

    def generateParenthesis_3(self, n):
        '''
        Try to use divide and conquer method.
        The idea is that p(n) = '(' p(n-1) ')' + ... '(' p(n-i-1) +')' p(i) + ... p(n-1)

        85 ms, 12.24% direct operating strings
        52 ms, 63.40% uses list and join the list afterwards
        '''
#        ans = [['']]
#        for i in range(1, n+1):
#            ans.append([])
#            for j in range(i):
#                for item1 in ans[j]:
#                    for item2 in ans[i-j-1]:
#                        ans[-1].append('('+item1+')'+item2)
#        return ans[-1]

        ans = [[[]]]
        for i in range(1, n+1):
            ans.append([])
            for j in range(i):
                for item1 in ans[j]:
                    for item2 in ans[i-j-1]:
                        ans[-1].append(['(']+item1+[')']+item2)
        return [''.join(item) for item in ans[-1]]



mysol = sol()
n = 4
print mysol.generateParenthesis(n)
print mysol.generateParenthesis_2(n)
print mysol.generateParenthesis_3(n)
