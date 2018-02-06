class sol(object):
    def search(self, nums, target):
        '''
        Suppose an array sorted in ascending order is rotated at some pivot 
        unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
        You are given a target value to search. If found in the array return its 
        index, otherwise return -1.
        Assume there is no duplicate.

        The basic idea of following script is consider different cases. But it seems
        that it fails for the situation when the target is outside the range of the
        number list.
        '''
        if nums:
            if nums[-1] >= nums[0]:
                return self.bisearch(nums, 0, len(nums)-1, target)
            else:
                return self.helper(nums, 0, len(nums)-1, target)
        return -1
    def helper(self, nums, left, right, target):
        if nums[right] < target < nums[left]:
            return -1
        mid = (left+right)/2
        if target >= nums[left]:
            if nums[mid] >= target:
                return self.bisearch(nums, left, mid, target)
            elif nums[mid] > nums[right]:
                return self.helper(nums, mid, right, target)
            else:
                return self.helper(nums, left, mid, target)
        elif target <= nums[right]:
            if nums[mid] <= target:
                return self.bisearch(nums, mid, right, target)
            elif nums[mid] > nums[right]:
                return self.helper(nums, mid, right, target)
            else:
                return self.helper(nums, left, mid, target)
    
    def bisearch(self, nums, left, right, target):
        '''
        Binary search method. Return -1 if not found.
        '''
        if target < nums[left] or target > nums[right]:
            return -1
        while left < right:
            mid = (left+right)/2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left if nums[left] == target else -1

    def search_2(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] <= nums[right]:
                return self.bisearch(nums, left, right, target)
            mid = (left+right)/2
            if target >= nums[left]:
                if target <= nums[mid]:
                    return self.bisearch(nums, left, mid, target)
                elif nums[mid] > nums[left]:
                    left = mid+1
                else:
                    right = mid-1
            elif target <= nums[right]:
                if target >= nums[mid]:
                    return self.bisearch(nums, mid, right, target)
                elif nums[mid] < nums[right]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                return -1
        return -1

    def search_3(self, nums, target):
        '''
        anther way to do is to firstly find the smallest numbers, 
        that's the place when the list is rotated. Then use the
        binary search on modified indexes to find the real index.
        '''
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)/2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
        temp = low
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            real = (mid+temp)%len(nums)
            if nums[real] == target:
                return real
            elif nums[real] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
    def search_4(self, nums, target):
        '''
        Actually don't need extra bisearch method. This can be done within the 
        framework of first binary search.
        '''

    def search_d(self, nums, target):
        '''
        Follow up the previous problem, what if duplicates are allowd?
        Would this affect the run-time complexity? How and why?

        It would increase the time complexity to find the pilot point using binary
        search.
        Looks this may break down because need to find the exact starting point 
        and ending point.
        '''
        low, high = 0, len(nums)-1
        ind = self.search_min(low, high, nums)
        while low <= high:
            mid = low+(high-low)/2
            realmid = (mid+ind)%len(nums)
            if nums[realmid] == target:
                return True
            elif nums[realmid] < target:
                low = mid+1
            else:
                high = mid-1
        return False
    def search_min(self, low, high, nums):
        if low >= high:
            return low 
        mid = low+(high-low)/2
        if nums[low] == nums[high]:
            left = self.search_min(low, mid, nums)
            right = self.search_min(mid+1, high, nums)
            if nums[left] < nums[right]:
                return left
            elif nums[left] >= nums[right]:
                return right
        if nums[high] < nums[mid]:
            return self.search_min(mid+1, high, nums)
        else:
            return self.search_min(low, mid, nums)
    def search_d_2(self, nums, target):
        '''
        Use linear search algo.
        42 ms, 79.95%
        '''
        for item in nums:
            if item == target:
                return True
        return False
    def search_d_3(self, nums, target):
        '''
        Binary search. Compare the value of low, mid and high, and then
        eliminate all duplicates.
        '''
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low+(high-low)/2
            if target == nums[mid]:
                return True
            while nums[low] == nums[mid] and low < mid:
                low +=1
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False
    def search_d_4(self, nums, target):
        '''
        Same idea, skip duplicates when nums[mid] == nums[mid]
        But this one may be a little bit slower? Or faster because
        binary search? Compared with search_d_3().
        42 ms, 78%
        '''
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low+(high-low)/2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid+1
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                low += 1
        return False

mysol = sol()
#nums = [3, 3, 5, 0, 0, 1, 3]
#target = 3
#print mysol.search_2(nums, target)
#print mysol.search_3(nums, target)
nums = [3, 1]
target = 1
print mysol.search_d_4(nums, target)
