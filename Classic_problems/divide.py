class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return -1
        if (dividend >= 0 and divisor < 0) or (dividend <= 0 and divisor >0):
            return -self.helper(abs(dividend), abs(divisor), {})
        return self.helper(abs(dividend), abs(divisor), {})
        
    def helper(self, dividend, divisor, mylist):
        if dividend < divisor:
            return 0
        ans = 0
        i = 1
        if 1 not in mylist.keys():
            mylist[1] = divisor
        while mylist[i] <= dividend:
            dividend -= mylist[i]
            ans += i
            mylist[i+i] = mylist[i]+mylist[i]
            i += i
        return ans+self.helper(dividend, divisor, mylist)

    def divide_bit(self, dividend, divisor):
        if divisor == 0:
            return -1
        sign = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
        if not sign:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)

    def divide_iter(self, dividend, divisor):
        if divisor == 0:
            return -1
        sign = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        mydict = {}
        while dividend >= divisor:
            temp, i = divisor, 1
            while temp <= dividend:
                if dividend in mydict.keys():
                    ans += mydict[dividend]
                    dividend = 0
                    break
                else:
                    mydict[dividend] = ans+i
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
        if not sign:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)


mysol = Solution()
print mysol.divide(-100, 3)
print mysol.divide_iter(-100, 3)
