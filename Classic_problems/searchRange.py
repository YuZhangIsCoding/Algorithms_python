class sol(object):
    def searchRange(self, nums, target):
        '''
        Given an array of integers sorted in ascending order, find the starting
        and ending position of a given target value.
        If the target is not found, return [-1, -1].
        The algorithm should be O(log(n))

        The idea is to first find the smallest number that is not less than
        the target, if it does not equal to the target, then the target is 
        not in nums. Else, search for the rest of the list to find the largest
        index of number that is no greater than target.
        '''
        ans = [-1, -1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if left < len(nums) and nums[left] == target:
            ans[0] = left
            right = len(nums)-1
            while left <= right:
                mid = (left+right)/2
                if nums[mid] > target :
                    right = mid-1
                else:
                    left = mid+1
            ans[1] = right
        return ans
    
    def searchRange_2(self, nums, target):
        '''
        Use devide and conquer methode. Find the block that contains target,
        return [-1, -1] if the block does not contain the target.
        '''
        if nums:
            return self.search_recursion(nums, 0, len(nums)-1)
        else:
            return [-1, -1]
    def search_recursion(self, nums, low, high):
        if nums[low] == target == nums[high]:
            return [low, high]
        if nums[low] <= target <= nums[high]:
            mid = (low+high)/2
            l = self.search_recursion(nums, low, mid)
            r = self.search_recursion(nums, mid+1, high)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]



mysol = sol()
nums = range(3)+[4]*4+range(5,10)
print nums
print [nums.index(i) for i in nums]
target = 4
print mysol.searchRange_2(nums, target)
