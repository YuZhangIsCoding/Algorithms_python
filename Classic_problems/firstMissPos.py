class Solution(object):
    def firstMissPos(self, nums):
        high = len(nums)
        low = 0
        for i in nums:
            if i <= 0 or i >= high:
                high -= 1
            if i == low+1:
                low += 1
        return min(low, high)+1

mysol = Solution() 
nums = [3,4,-1,1]
nums = [2, 1]
print mysol.firstMissPos(nums)
