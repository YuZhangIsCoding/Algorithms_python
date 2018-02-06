class sol(object):
    def combine(self, n, k):
        '''
        Insert the number larger than the last number only
        Memory limit exceed.
        '''
        if n < k:
            return []
        ans = [[i] for i in range(1, n-k+2)]
        while k-1 > 0:
            temp = []
            for item in ans:
                for i in range(item[-1]+1, n+1):
                    temp.append(item+[i])
            k -= 1
            ans = temp
        return ans
    def combine_2(self, n, k):
        '''
        Uses recursion to do the iterations.
        '''
        ans = []
        self.recursion(ans, 1, k, [], n)
        return ans
    def recursion(self, ans, start, k, temp, n):
        '''
        Skip the recursions when there's no enough numbers left.
        '''
        if n+2-start <= k:
            return
        while k > 0:
            for i in range(start, n+1):
                temp.append(i)
                self.recursion(ans, i+1, k-1, temp, n)
                temp.pop()
            return
        ans.append(temp[:])
        return

######## subset 1 ########
    def subsets(self, nums):
        '''
        Given a set of distinct integers, return all possible subsets.

        Basically the same idea as combination, but we return temp every step.
        '''
        ans = [[]]
        self.sub_recur(nums, 0, [], len(nums), ans)
        return ans
    def sub_recur(self, nums, start, temp, n, ans):
        for i in range(start, n):
            temp.append(nums[i])
            self.sub_recur(nums, i+1, temp, n, ans)
            ans.append(temp[:])
            temp.pop()
        return
    def subsets_2(self, nums):
        '''
        Iterative way. There are totally 2^n combinations, each iteration add
        a number or don't.
        '''
        ans = [[]]
## The while loop could be replaced by for loop
#        while nums:
#            temp = nums.pop()
        for temp in nums:
            ans += [item+[temp] for item in ans]
        return ans

####### subsets 2 #######
    def subsetsWithDup(self, nums):
        '''
        Follow up the previous problem, what if a collection of integers 
        might contain duplicates.
        May not contain duplicates for the output.

        The idea is to eliminate duplicates by combinin the duplicated numbers
        together as a new item to append to the existing list.
        52 ms, 99.22%
        '''
        ans = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            ## multiple ways to do this block, but it seem this one is really fast.
            ## e.g. use append in the loop.
            count = 0
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                count += 1
                i += 1
            ilist = [[nums[i]]*item for item in xrange(1, 2+count)]
            temp = ans[:]
            for item in ilist:
                ans += [j+item for j in temp]
            i += 1
        return ans
    def subsetsWithDup_2(self, nums):
        '''
        The idea is to mark each time the index inserted, if meet a duplicate,
        only append that element to elements starting from last insert.

        55 ms, 95.17%
        '''
        ans = [[]]
        nums.sort()
        last = 0
        for i in range(len(nums)):
            temp = len(ans)
            if i > 0 and nums[i] == nums[i-1]:
                ans += [item+[nums[i]] for item in ans[last:]]
            else:
                ans += [item+[nums[i]] for item in ans]
            last = temp
        return ans
    def subsetsWithDup_3(self, nums):
        '''
        Recursive solution. The idea is that if meet a duplicate number,
        itself can be added the path (i == ind), but skip the recursion
        ( i > ind).
        '''
        ans = []
        self.subsetDup_recur(nums, 0, [], ans)
        return ans
    def subsetDup_recur(self, nums, ind, path, ans):
        ans.append(path)
        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i-1]:
                continue
            npath = path+[nums[i]]
            print npath
            self.subsetDup_recur(nums, i+1, npath, ans)


                    
mysol = sol()
#print mysol.combine_2(4,3)
#print len(mysol.combine_2(20, 16))

## subset 1
#print mysol.subsets_2(range(3))

## subsets with duplicates
nums = [1,1,2, 2, 2]
print len(mysol.subsetsWithDup(nums))
print len(mysol.subsetsWithDup_2(nums))
print len(mysol.subsetsWithDup_3(nums))
