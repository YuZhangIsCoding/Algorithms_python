class sol(object):
    def removeDuplicates(self, nums):
        '''
        Given a sorted array, remove duplicates in place such that each element
        appear only once and return the new length.
        Do not allocate extra space for another array
        In place with constant memory

        Most intuitive way, once encounter duplicates, pop it from the list
        '''
        if len(nums) <= 1:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return i

    def removeDuplicates_2(self, nums):
        '''
        The other way is to use 2 pointers
        '''
        if not nums:
            return 0
        i = 1
        for j in range(1, len(nums)):
            if nums[j-1] < nums[j]:
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates_ii(self, nums):
        '''
        Follow up for remove duplicates
        what if duplicates are allowed at most twice.
        
        The idea is count the duplicate numbers, only when the count is smaller
        than 2, the number will be put in the head of list.
        62 ms, 82.15%
        '''
        if len(nums) <= 2:
            return len(nums)
        i = 1
        count = 0
        for j in range(1, len(nums)):
            if nums[j-1] < nums[j]:
                count = 0
            else:
                count += 1
            if count < 2:
                nums[i] = nums[j]
                i += 1
        return i

    def removeDuplicates_ii_2(self, nums):
        '''
        This one is far more concise. Instead of tracking faster pointer,
        we just need to compare the faster pointer with the number on the left
        side of slow pointer. In other words, we just need to make sure that 
        the slow pointer does not have more than 2 duplicates.
        '''
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
mysol = sol()
#nums = [1,1,1,2,3,4]
#print nums[:mysol.removeDuplicates_2(nums)]
nums = [1,1,1,2,2,2,3]
print nums[:mysol.removeDuplicates_ii_2(nums)]
