class Solution(object):
    def multiply(self, num1, num2):
        ans = 0
        backup ={}
        for item in num2:
            if item not in backup.keys():
                temp = 0
                for i in num1:
                    temp = temp*10+int(item)*int(i)
                backup[item] = temp
            ans = ans*10+backup[item]
        return str(ans)
    def multi_comp(self, num1, num2):
        mydict = {'0': 0, '1': 1, '2': 2, '3': 3,\
                '4': 4, '5': 5, '6': 6, '7': 7,\
                '8': 8, '9': 9}
        ans = 0
        back = {}
        for item in num2:
            if item not in back.keys():
                temp = 0
                for i in num1:
                    temp = temp*10+mydict[i]*mydict[item]
                back[item] = temp
                ans = ans*10+temp
            else:
                ans = ans*10+back[item]
        return str(ans)

mysol = Solution()
num1 = '123'
num2 = '456'
print int(num1)*int(num2)
print mysol.multiply(num1, num2)
print mysol.multi_comp(num1, num2)
