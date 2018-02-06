class sol(object):
    def permute(self, nums):
        '''
        Given a collection of distinct numbers, return all possible permutations.
        [1,2] has the permutations of [[1, 2], [2, 1]]
        The idea is that there is a len(list)+1 way to insert a new number in the list.
        Iterate the process until all numbers used.
        '''
        ans = [[]]
        for i in nums: 
            temp = []
            for item in ans:
                for ndx in range(len(item)+1):
                    temp.append(item[:ndx]+[i]+item[ndx:])
            ans = temp
        return ans
    def permute_2(self, nums):
        '''
        The idea is to swap 2 nums and put it in a list
        '''
        ans = []
        self.per_recursion(nums, 0, len(nums), ans)
        return ans
    def per_recursion(self, nums, i, j, ans):
        if i == j-1:
            ans.append(nums[:])
            return
        for k in range(i, j):
            ## The if command below works for removing duplicates.
            if i != k and nums[i] == nums[k]:
                continue
            nums[i], nums[k] = nums[k], nums[i]
            self.per_recursion(nums, i+1, j, ans)
        return


    def permuteUnique(self, nums):
        '''
        Given a collection of numbers that might contain duplicates, return all possible 
        unique permutations.
        Try that for the duplicated numbers, they can only be inserted in the slots after
        previous numbers.
        '''
        ans = [[]]
        ## not necessary to sort the nums, but may speed up the whole processes?
        ## Actually, the sort won't help, because the total steps are the same N!.
        ## nums.sort()
        for i in nums:
            temp = []
            for item in ans:
                for ndx in range(len(item), -1, -1):
                    temp.append(item[:ndx]+[i]+item[ndx:])
                    ndx -= 1
                    if ndx >= 0 and i == item[ndx]:
                        break
            ans = temp
        return ans

    def getPermut(self, n, k):
        '''
        The idea is to first build a dictionary to pop out the most significant digits
        each time until the sum of their permutation is equal to k.
        '''
        mylist = {1: 1}
        orig = [str(i) for i in range(1, n+1)]
        cur = 1
        while k > mylist[cur]:
            cur += 1
            mylist[cur] = mylist[cur-1]*cur
        ans = [orig.pop(0) for i in range(n-cur)]
        k -= 1
        while len(orig) > 0 and k > 0:
            ans.append(orig.pop(k/mylist[len(orig)-1]))
            k = k%mylist[len(orig)]
        return ''.join(ans+orig)

    def nextPermutation(self, nums):
        '''
        Given an array of numbers, rearrange the numbers into lexicographically
        next greater permutation of numbers.
        If no such arrangement, rearrange it as the lowest possible order.
        Implement it in-place, and do not allocate extra memory.

        The basic idea is that if all the numbers in current block is in descending
        order, we move to a more significant digit (move left). Otherwise, we do
        following:
        Iterate in current block, for each num, find the smallest number that is 
        larger than num and its larger than num. If found, switch the two values.
        Because of case 1, all of the numbers except the first number in this block
        are in descending order, all we need to do then is reserve the position of them
        in the block.
        '''
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    k, m = i+1, len(nums)-1
                    while k < m:
                        nums[k], nums[m] = nums[m], nums[k]
                        k += 1
                        m -= 1
                    return
        i, j = 0, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

    def nextPermutation_2(self, nums):
        '''
        Actually we can put the if statement outside the second for loop, so that it could
        be O(n).
        '''
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1 and nums[i+1] > nums[i]:
                for j in range(len(nums)-1, i, -1):
                    nums[i], nums[j] = nums[j], nums[i]
                    k, m = i+1, len(nums)-1
                    while k < m:
                        nums[k], nums[m] = nums[m], nums[k]
                        k += 1
                        m -= 1
                    return
        i, j = 0, len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return

mysol = sol()
#print mysol.getPermut(3, 4)
#print mysol.permute(range(4))
#print mysol.permute_2(range(4))
#print len(mysol.permute(range(9)))
#print mysol.permuteUnique([2,2,1,1])
nums = [1, 3, 2]
print nums
mysol.nextPermutation(nums)
print nums
