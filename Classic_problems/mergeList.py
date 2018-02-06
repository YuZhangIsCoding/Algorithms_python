class sol(object):
    def merge(self, nums1, m, nums2, n):
        '''
        Given two sorted arrays nums1 and nums2, merge nums2 into nums1
        as one sorted array.
        May assume that nums1 has enough space (>= m+n) to hold all elements
        from nums2. The number initialized in nums1 and nums2 are m and n 
        repectively.

        The idea is to first find the insertion point of nums2 in nums1,
        and then swaping the numbers accordingly.
        42 ms, 83.77%
        '''
        p = 0
        r = 0
        temp = []
        while p < n:
            while r < m and nums1[r] <= nums2[p]:
                r += 1
            temp.append(r)
            p += 1
        p = n-1
        r = m
        while r >= 0:
            if p >= 0 and r == temp[p]:
                    nums1[r+p] = nums2[p]
                    p -= 1
            elif p >= 0:
                nums1[r+p] = nums1[r-1]
                r -= 1
            else:
                r -= 1
        return
    def merge_2(self, nums1, m, nums2, n):
        '''Rethink of the previous one, we don't actually needs a
        list, we can do it in just one loop. But need to start from
        the end.

        39 ms, 95.77%
        '''
        n -= 1
        while m >= 0 and n >= 0:
            if m > 0 and nums1[m-1] < nums2[n]:
                nums1[m+n] = nums2[n]
                n -= 1
            elif m > 0:
                nums1[m+n] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n] = nums2[n]
                n -= 1
        return
    def merge_3(self, nums1, m, nums2, n):
        '''Actually the case 1 and case 3 in previous code can be
        combined to combame more concise. But seems not fast enough
        '''
        n -= 1
        while m >= 0 and n >= 0:
            if m == 0 or nums1[m-1] < nums2[n]:
                nums1[m+n] = nums2[n]
                n -= 1
            else:
                nums1[m+n] = nums1[m-1]
                m -= 1
        return

mysol = sol()
import random
def test(num_trials = 100):
    for _ in range(num_trials):
        nums1 = sorted([random.randint(0, 10) for i in range(8)])
        nums2 = sorted([random.randint(0,10) for i in range(3)])
##        nums1 = [1, 3, 3, 4, 4, 5, 10, 10]
##        nums2 = [0, 6, 9]
##        print nums1
##        print nums2
        ref = sorted(nums1[:5]+nums2)
        mysol.merge_3(nums1, 5, nums2, 3)
##        print nums1
        if not ref == nums1:
            print 'Failed'
            break
    print 'Succeed'
test()
