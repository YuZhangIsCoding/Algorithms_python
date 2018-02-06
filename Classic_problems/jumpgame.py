class Sol(object):
    def canjump(self, nums):
        '''
        The idea is to compare max jump length with the current jump length.
        O(N)
        '''
## 72 ms, 26.82
        if not nums:
            return True
        i, temp = 0, 0
        while i <= temp:
            temp = max(i+nums[i], temp)
            if temp >= len(nums)-1:
                return True
            i += 1
        return False
    def canjump_concise(self, nums):
        '''
        Reduce lines to be more concise
        '''
        i, temp = 0, 0
        while i <= temp and i < len(nums):
            temp = max(i+nums[i], temp)
            i += 1
        return temp >= len(nums)-1
    
    def canjump_2(self, nums):
        '''
        Using the same idea, but could we start from higher index?
        The time complexity varies, with the worst situation of
        O(n^2) if large jump number at at beginning of the list.
        But tests show that this one is faster than previous O(N)
        solution.
        '''
## 49ms, 90.69%
        i, temp = 0, 0
        while i >= 0:
            if nums[i]+i > temp:
                temp =  nums[i]+i
                i = temp
            else:
                i -= 1
            if temp >= len(nums)-1:
                return True
        return False
    def canjump_3(self, nums):
## 72ms, 26.82%
        cur = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= cur:
                cur = i
        return not cur
    def canjump_4(self, nums):
        '''
        Dynamic programming with memory table
        '''
        return
    def canjump_5(self, nums):
        '''
        The idea is that, the list fails to jump to the end only when
        there are 0 and the previous index cannot jump over it.
        So we just need to check when there are zeros.
        '''
## 56 ms, 69.89%
        if len(nums) <= 1:
            return True
#        for i in range(len(nums)-2, -1, -1):
        i = len(nums)-2
        while i >= 0:
            if nums[i] == 0:
                gap = 1
                while nums[i] < gap:
                    gap += 1
                    i -= 1
                    if i < 0:
                        return False
            i -= 1
        return True

    def jump(self, nums):
        '''
        Assume we can always reach the last index, find the minimum number
        of jumps.
        '''
        if len(nums) == 1:
            return 0
        i, low, high = 0, 0, 0
        count = 0
        while i < len(nums)-1:
            high = max(high, i+nums[i])
            if high >= len(nums)-1:
                return count+1
            if i == low:
                low = high
                count += 1

    def jump_2(self, nums):
        '''
        The use of while loop avoid the if statement in jump()
        '''
        i, low, high = 0, 0, 0
        count = 0
        while i < len(nums)-1:
            high = max(high, i+nums[i])
            if high >= len(nums)-1:
                return count+1
            if i == low:
                low = high
                count += 1
            i += 1



mysol = Sol()
#nums = [3,2,1,0,4]
nums = [2,3,1,1,4]
nums = [2,1,3,4,5,1,1,4,2]
nums = [0]
#print mysol.canjump(nums)
#print mysol.canjump_2(nums)
#print mysol.canjump_3(nums)
#print mysol.canjump_5(nums)
print mysol.jump(nums)
