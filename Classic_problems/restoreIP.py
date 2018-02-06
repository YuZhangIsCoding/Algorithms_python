class sol(object):
    def restoreIpAddresses(self, s):
        '''
        Given a string containing only digits, restore it by returning all 
        possible valid IP address combinations.
        
        Some backgroudn knowledge:
        The IPv4 address is 32-bit (4-byte) in size, and are usually represented
        in dot-decimal notation, consisting of 4 decimal numbers, each ranging
        from 0 to 255.

        Thinking: pay attention to 0 in the string, two 0 can not be put together.
        '''
        if len(s) > 12:
            return []
        ans = []
        return ans

mysol = sol()
s = '0000'
print mysol.restoreIpAddresses(s)
