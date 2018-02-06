class sol(object):
    def grayCode(self, n):
        '''
        The gray code is a binary numeral system where two successive values
        differ in only one bit.
        A gray code must starts with 0. For a given number n, print the sequence
        of gray code.

        The idea is to build lists based on previous lists. And then convert the
        list to real number.
        '''
        ans = [[]]
        for i in range(n):
            temp1 = []
            temp2 = []
            for item in ans:
                temp1.append(item+[0])
                temp2.append(item+[1])
            ans = temp1+temp2[::-1]
        temp = []
        for item in ans:
            temp.append(self.list2num(item))
        return temp
    def list2num(self, mylist):
        ans = 0
        for item in mylist:
            ans = 2*ans +item
        return ans

    def grayCode_2(self, n):
        '''
        But actually we can just manipulate the numbers directly.

        42 ms, 82.28%
        35 ms, 99.17% save 2**i to dig, save a lot time
        '''
        ans = [0]
        dig = 1
        for i in range(n):
            temp = []
            for item in ans[::-1]:
                temp.append(dig+item)
            ans += temp
            dig *= 2
        return ans
    def grayCode_3(self, n):
        '''
        Bit operation ^:
        Each bit of the output is the same as the corresponding bit in x
        if that bit in y is 0, and it's the complement of the bit in x
        if that bit in y is 1.
        More about gray code: https://en.wikipedia.org/wiki/Gray_code
        '''
        ans = []
        for i in range(1<<n):
            ans.append(i^i>>1)
        return ans
        
mysol = sol()
print mysol.grayCode_3(4)
