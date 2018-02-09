import heapq
import operator

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
    def HeapSort(self, nums):
        '''python has provided an implementation of priority queue algorithm
        heapq. Use this library to implement heapsort by pushing all values
        onto a heap and then popping off the smallest values at a time.
        '''
        h = []
        for value in nums:
            heapq.heappush(h, value)
        ## or could just use heapq.heapify(nums) to transform a list into heap.
        return [heapq.heappop(h) for i in range(len(h))]
    def HeapSort_inplace(self, nums):
        '''The previous heapsort using builtin heapq may require extra O(n)
        spaces. We could however implement a inplace heapsort that swaps values
        in the list, which only needs O(1) extra space.
        '''
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            self.heapify(nums, n, i)
        while n > 1:
            nums[0], nums[n-1] = nums[n-1], nums[0]
            n -= 1
            self.heapify(nums, n, 0)
        return nums
    def heapify(self, nums, n, i, compare = operator.gt):
        '''Assume that that trees rooted at left and right child of i are 
        already heap tree. heapify() corrects the violation at i.
        n is useful to maintain the space O(1) by swap values inplace.
        Default is to maintain a max heap, but can easily modified to get a min
        heap.
        '''
        left = 2*i+1
        right = left+1
        if left < n and compare(nums[left], nums[i]):
            extreme = left
        else:
            extreme = i
        if right < n and compare(nums[right], nums[extreme]):
            extreme = right
        if extreme != i:
            nums[extreme], nums[i] = nums[i], nums[extreme]
            self.heapify(nums, n, extreme)
        
        

mysol = sol()
import random
##rad = [random.randint(0, 100)  for _ in range(10)]
##print mysol.mergeSort(rad)
##rad = [random.randint(0, 2) for _ in range(10)]
##print rad
##mysol.sortColor_2(rad)
##print rad

## comparison of merge sort and counting sort, counting sort is much faster ##
nums = [random.randint(0, 1000) for _ in range(100000)]
import time
time1 = time.time()
mysol.mergeSort(nums)
time2 = time.time()
mysol.countingSort(nums)
time3 = time.time()
## Can do inplace but here will modify the nums
mysol.QuickSort(nums[:])
time4 = time.time()
mysol.HeapSort(nums)
time5 = time.time()
mysol.HeapSort_inplace(nums)
time6 = time.time()
print 'merge sort:', time2-time1
print 'counting sort', time3-time2
print 'quick sort', time4-time3
print 'heap sort(using heapq)', time5-time4
print 'heap sort(inplace)', time6-time5
