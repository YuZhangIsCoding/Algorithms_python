class sol(object):
    def mergeSort(self, nums):
        '''
        Merge sort: use recursion to break down into 2 sorted lists and merge.
        O(nlog(n))
        '''
        if len(nums) < 2:
            return nums
        else:
            return self.merge(self.mergeSort(nums[:len(nums)/2]), \
                              self.mergeSort(nums[len(nums)/2:]))
    def merge(self, num1, num2):
        '''
        merge 2 sorted lists
        '''
        i = 0
        j = 0
        ans = []
        while i < len(num1) and j < len(num2):
            if num1[i] <= num2[j]:
                ans.append(num1[i])
                i += 1
            else:
                ans.append(num2[j])
                j += 1
        if i < len(num1):
            ans += num1[i:]
        if j < len(num2):
            ans += num2[j:]
        return ans
    def sortColor(self, nums):
        '''
        Sorted colors
        Integers 0, 1, and 2 to represent the color red, white
        Modify nums in place
        '''
        p0, p2 = 0, len(nums)-1
        for pc in range(len(nums)):
            while nums[pc] == 2 and pc < p2:
                nums[pc], nums[p2] = nums[p2], nums[pc]
                p2 -= 1
            while nums[pc] == 0 and pc > p0:
                nums[pc], nums[p0] = nums[p0], nums[pc]
                p0 += 1
        return
    def sortColor_2(self, nums):
        '''
        we could just count the number of each color and
        assign them afterwards
        '''
        c0, c1 = 0, 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
        p = 0
        for p in range(len(nums)):
            if p < c0:
                nums[p] = 0
            elif p < c0+c1:
                nums[p] = 1
            else:
                nums[p] = 2
        return
    def countingSort(self, nums):
        k = max(nums)+1
        counter = [[] for _ in range(k)]
        for i in nums:
            counter[i].append(i)
        ans = []
        for i in range(k):
            ans.extend(counter[i])
        return ans
    def QuickSort(self, nums):
        self.QuickSort_recur(nums, 0, len(nums)-1)
        return nums
    def QuickSort_recur(self, nums, lower, higher):
        if higher-lower < 1:
            return
        pivot = (lower+higher)//2
        nums[pivot], nums[higher] = nums[higher], nums[pivot]
        p1 = lower
        p2 = higher-1
        while p1 <= p2:
            if nums[p1] <= nums[higher]:
                p1 += 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
        nums[p1], nums[higher] = nums[higher], nums[p1]
        self.QuickSort_recur(nums, lower, p1-1)
        self.QuickSort_recur(nums, p1+1, higher)
        return


        

mysol = sol()
import random
##rad = [random.randint(0, 100)  for _ in range(10)]
##print mysol.mergeSort(rad)
##rad = [random.randint(0, 2) for _ in range(10)]
##print rad
##mysol.sortColor_2(rad)
##print rad

## comparison of merge sort and counting sort, counting sort is much faster ##
nums = [random.randint(0, 1000) for _ in range(10000)]
import time
time1 = time.time()
mysol.mergeSort(nums)
time2 = time.time()
mysol.countingSort(nums)
time3 = time.time()
mysol.QuickSort(nums)
time4 = time.time()
print 'merge sort:', time2-time1
print 'counting sort', time3-time2
print 'quick sort', time4-time3
