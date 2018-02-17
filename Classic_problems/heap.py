import random
class min_heap(object):
    def __init__(self, iterable = [], inplace = False):
        if inplace:
            self.h = iterable
        else:
            self.h = iterable[:]
        for i in range(len(self.h)//2-1, -1, -1):
            self.heapify(i)
        ## the following will work for all iterables, but the complexity is 
        ## O(nlgn)
        ## self.h = []
        ## for item in iterable:
        ##     self.append(item)
    def append(self, item):
        '''Insert an item into heap. First append the item to the end of the
        list, but this may change the heap invariant. So we need to correct
        outliers from bottom up.
        '''
        self.h.append(item)
        cur = len(self.h)-1
        parent = (cur+1)//2-1
        while cur > 0 and self.h[cur] < self.h[parent]:
            self.h[cur], self.h[parent] = self.h[parent], self.h[cur]
            cur = parent
            parent = (cur+1)//2-1
    def heapify(self, index):
        if index < 0:
            index = len(self.h)+index
        left = index*2+1
        right = left+1
        if left < len(self.h) and self.h[left] < self.h[index]:
            smallest = left 
        else:
            smallest = index
        if right < len(self.h) and self.h[right] < self.h[smallest]:
            smallest = right
        if smallest != index:
            self.h[smallest], self.h[index] = self.h[index], self.h[smallest]
            self.heapify(smallest)
    def get(self, index):
        return self.h[index]
    def pop(self):
        self.h[0], self.h[-1] = self.h[-1], self.h[0]
        temp = self.h.pop()
        self.heapify(0)
        return temp

class tuple_heap(min_heap):
    def append(self, item, compare = lambda x, y: x[0] < y[0]):
        self.h.append(item)
        cur = len(self.h)-1
        parent = (cur+1)//2-1
        while cur > 0 and compare(self.h[cur], self.h[parent]):
            self.h[cur], self.h[parent] = self.h[parent], self.h[cur]
            cur = parent
            parent = (cur+1)//2-1
    def heapify(self, index, compare = lambda x, y: x[0] < y[0]):
        if index < 0:
            index = len(self.h)+index
        left = index*2+1
        right = left+1
        if left < len(self.h) and compare(self.h[left], self.h[index]):
            extreme = left 
        else:
            extreme = index
        if right < len(self.h) and self.h[right] < self.h[extreme]:
            extreme = right
        if extreme != index:
            self.h[extreme], self.h[index] = self.h[index], self.h[extreme]
            self.heapify(extreme)

def kminheap(nheap, k, n):
    '''
    Present an O(klgk) time algorithm to return the kth minimum element in a 
    min-heap H of size n.

    The idea is to keep track of the candidates of the smallest kth item using
    a heap.
    '''
    kheap = tuple_heap()
    kheap.append((nheap.get(0), 0))
    for i in range(k):
        (val, index) = kheap.pop()
        if i == k-1:
            return val
        if 2*index+1 < n:
            kheap.append((nheap.get(2*index+1), 2*index+1))
        if 2*index+2 < n:
            kheap.append((nheap.get(2*index+2), 2*index+2))

def test(n):
    count = 0
    for i in range(n):
        mylist = [random.randint(10, 100) for _ in range(10)]
        nheap = min_heap(mylist)
        if sorted(mylist)[4] == kminheap(nheap, 5, 10):
            print 'Pass'
            count += 1
        else:
            print 'Fail value should be:', sorted(mylist)[4]
    print 'Success rate:', float(count)/n
test(10)
