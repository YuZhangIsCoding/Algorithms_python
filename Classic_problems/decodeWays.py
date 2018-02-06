class sol(object):
    def numDecoding(self, s):
        '''
        A message containing letters from A-Z is being encoded to numbers
        using the following mapping:
        A -> 1
        ...
        Z -> 26
        Given an encoded message containing digits, determine the total number
        of ways to decode it.

        The idea of following code is to count of useful double interpretations.
        '''
        if not s or s[0] == '0':
            return 0
        count = 0
        for i in range(len(s)-1):                                                                           
            if s[i+1] == '0':
                if int(s[i]) > 2 or s[i] == '0':
                    return 0
            elif 10 < int(s[i:i+2]) <= 26:
                if i+2 < len(s):
                    if s[i+2] != '0':
                        count += 1
                else:
                    count += 1
        return count


mysol = sol()
s = '1212'
print mysol.numDecoding(s)
