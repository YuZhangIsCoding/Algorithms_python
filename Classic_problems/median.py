class sol(object):
    def findMedianSoortedArray(self, num1, nums2):
        '''
        Find the mdiean of two sorted arrays.
        The overall run time complexity should be O(log(m+n))

        Try 4-pointer. Two of them starts from the beginning of each list.
        And the other two starts from the end of each list. Keep record of 
        low and high values when they both move towards center, until one 
        of the lists is thoroughly screened. Find the median of the rest
        of elements in the other list.

        Oops, the time complexity is O(m) instead of O(log(m+n)), need to
        implement something like binary search.
        '''
        p1, p2 = 0, len(num1)-1
        p3, p4 = 0, len(num2)-1
        while p1 <= p2 and p3 <= p4:
            if num1[p1] < num2[p3]:
                low = num1[p1]
                p1 += 1
            else:
                low = num2[p3]
                p3 += 1
            if num1[p2] > num2[p4]:
                high = num1[p2]
                p2 -= 1
            else:
                high = num2[p4]
                p4 -= 1
        while p1 <= p2:
            low = num1[p1]
            high = num1[p2]
            p1 += 1
            p2 -= 1
        while p3 <= p4:
            low = num2[p3]
            high = num2[p4]
            p3 += 1
            p4 -= 1
        return (low+high)/2.0

    def findMedianSoortedArray_2(self, nums1, nums2):
        '''
        Need to use binary search for the two lists together.
        '''
        low1, high1 = 0, len(nums1)
        low2, high2 = 0, len(nums2)
        while low1 <= high1 and low2 <= high2:
            mid1 = (low1+high1)/2
            mid2 = (low2+high2)/2
        return

mysol = sol()
num1 = [1,2]
num2 = [3,4]
num1 = [1, 2, 4]
num2 = [3, 4, 5]
#num1 = [1,2,3,10]
#num2 = [2, 9, 29, 30, 70, 100]
import random
num1 = sorted([random.randint(0, 10) for _ in range(6)])
num2 = sorted([random.randint(0, 10) for _ in range(7)])
nums = sorted(num1+num2)
print num1, num2
print nums
print (nums[len(nums)/2-1]+nums[len(nums)/2])/2.0
print mysol.findMedianSoortedArray(num1, num2)
print mysol.findMedianSoortedArray_2(num1, num2)

