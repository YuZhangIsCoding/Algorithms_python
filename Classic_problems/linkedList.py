import operator
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        ans = []
        while self:
            ans.append(str(self.val))
            self = self.next
        return 'SL-list ['+', '.join(ans)+']' 
def cast_list(mylist):
    '''
    This is a function to convert a list into single linked lists.
    '''
    if not mylist:
        return ListNode(None)
    ans = temp = ListNode(mylist[0])
    for item in mylist[1:]:
        temp.next = ListNode(item)
        temp = temp.next
    return ans

class sol(object):
    def addTwoNumbers(self, l1, l2):
        '''
        Given two none-empty linked lists representing 2 non-negative integers.
        Add the two numbers and return it as a linked list
        (2, 4, 3)+(4, 6, 4) = (6, 0, 8)

        122 ms, 85.33%

        Follow up the previous question. What if the numbers are stored in 
        non-reverse order? Probably need to go over the whole lists first
        to determine the digits.
        (2, 4, 3)+(4, 6, 4) = (7, 0, 7)
        '''
        up = 0
        ans = temp = ListNode(0)
        while l1 or l2 or up:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            temp.next = ListNode((v1+v2+up)%10)
            temp = temp.next
            up = (v1+v2+up)/10
        return ans.next
    
    def addTwoNumbers_2(self, l1, l2):
        '''
        Much more concise one.
        '''
        carry = 0
        addend = l1, l2
        dummy = temp = ListNode(0)
        while addend or carry:
            carry += sum(item.val for item in addend)
            addend = [item.next for item in addend if item.next]
            ## This line here is quite interesting does equal to 
            ## temp.next = ListNode(); temp = temp.next
            temp.next = temp = ListNode(carry%10)
            carry = carry/10
        return dummy.next

####### remove Nth Node From End of list ##########
    def removeNthFromEnd(self, head, n):
        '''
        Given a linked list, remove the nth node from the list
        and return its head

        46ms, 79%
        42ms, 95.34%
        '''
        ans = head
        p1 = p2 = 0
        while head:
            p2 += 1
            if p2-p1 == n:
                if p1 == 1:
                    pre = ans
                    track = pre.next
                elif p1 > 1:
                    pre = track
                    track = track.next
                p1 += 1
            head = head.next
        if p1 == 1:
            return ans.next
        pre.next = pre.next.next
        return ans

    def removeNthFromEnd_2(self, head, n):
        '''
        Instead of judging whether the element to be removed is the first node.
        We could first add a dummy node to the head of the list.
        This reduces the corner cases.

        46 ms, 79%
        '''
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = 0
        pre = dummy
        while head:
            p2 += 1
            if p2-p1 == n:
                if p1 > 0:
                    pre = pre.next
                p1 += 1
            head = head.next
        pre.next = pre.next.next
        return dummy.next

    def removeNthFromEnd_3(self, head, n):
        '''
        Rewrite the previous one using 2 loop, could save some variables.
        42 ms, 95.34%
        '''
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for count in range(n):
            head = head.next
        while head:
            pre = pre.next
            head = head.next
        pre.next = pre.next.next
        return dummy.next

###### Merge two sorted linked lists ########
    def mergeTwoLists(self, l1, l2):
        '''
        52 ms, 75.55%
        '''
        dummy = temp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                temp.next =  ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val) 
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return dummy.next
## This following code can be further reduced by temp.next = l1 or l2
#        if l1:
#            temp.next = l1
#        if l2:
#            temp.next = l2
#        return dummy.next

## Actually we do not need to append that again, we just need to 
## append the remaining list to the temp.next. 
## The following content was commentted out.
#        while l1:
#            temp.next = ListNode(l1.val)
#            temp = temp.next
#            l1 = l1.next
#        while l2:
#            temp.next = ListNode(l2.val)
#            temp = temp.next
#            l2 = l2.next
#        return dummy.next

    def mergeTwoLists_2(self, l1, l2):
        '''
        Try to be concise.
        The list method need to consider duplicates.
        '''
        dummy = temp = ListNode(0)
        com = [l1, l2]
        while com:
            val = [item.val for item in com if item.val]
            for item in val:
                if item == min(val):
                    temp.next = ListNode(item)
                    temp = temp.next
            com = [item.next if item.val == min(val) else item for item in com if item.next]
        return dummy

    def mergeTwoLists_3(self, l1, l2):
        '''
        Recursive way. No additional variable defined.
        quote "But may be a terrible solution from a practical point of view because
        the stack size would be equal to the length of the merged list, and may
        result in overflow for relatively small lists." But that's basically the problem
        for many recursive algorithms.
        
        49 ms, 90.70%. The actual test speed is fast.
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_3(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_3(l1, l2.next)
            return l2

######## merge k sorted lists ########
    def mergeKLists(self, lists):
        '''
        Merge k sorted linked lists and return it as one sorted list.
        The time complexity is O(m^2*n) n is the length of list, m is 
        the length of lists.
        '''
        dummy = temp = ListNode(0)
        while lists:
            vals = []
            for nl in lists:
                if nl and nl.val != None:
                    vals.append(nl.val)
            if not vals:
                break
            mv = min(vals)
            empty = []
            for nl in lists:
                if nl and nl.val == mv:
                    temp.next = ListNode(mv)
                    temp = temp.next
                    empty.append(nl.next)
                elif nl:
                    empty.append(nl)
            lists = empty
        return dummy.next

    def mergeKLists_2(self, lists):
        '''
        Utilized the previous merge two lists functions.
        Timelimit exceed for this case.
        Merge m-1 times.
        '''
        temp = ListNode(None)
        for nl in lists:
            if nl and nl.val != None:
                if temp.val == None:
                    temp.next = nl
                    temp = temp.next
                else:
                    temp = self.mergeTwoLists_3(temp, nl)
        if temp.val != None:
            return temp
        else:
            return None 
    
    def mergeKLists_3(self, lists):
        '''
        The idea is to keep the lists sorted by the node's val. Each time 
        pop out the lowest value and append the next node. Reorgize the list
        and repeat the process until the list only contain one node.

        139 ms, 77.93%, first try
        132 ms, 82.86%, check mylist
        '''
        dummy = temp = ListNode(0)
        mylist = [nl for nl in lists if nl and nl.val != None]
        mylist = sorted(mylist, key = operator.attrgetter('val'))
        while mylist:
            empty = mylist.pop(0)
            temp.next = empty
            temp = temp.next
            if mylist and empty.next and empty.next.val != None:
                mylist = self.sort_KList(mylist, empty.next)
        return dummy.next
    
    def sort_KList(self, mylist, target):
        '''
        This is a helper function for mergeKLists_3 to sort out the list.
        The first n-1 items already sorted, need to insert the last item
        into the list using binary search.
        '''
        low, high = 0, len(mylist)-1
        while low <= high:
            mid = (low+high)/2
            if mylist[mid].val == target.val:
                return mylist[:mid]+[target]+mylist[mid:]
            if mylist[mid].val < target.val:
                low = mid+1
            else:
                high = mid-1
        return mylist[:low]+[target]+mylist[low:]

######## swap nodes ########
    def swapPairs(self, head):
        '''
        Given a linked list, swap every two adjacent nodes and return its head
        Do not modify values in the list, only the node itself.
        Use constant space.

        The idea is to use keep track of 3 nodes and swap when a pair is found.
        39 ms, 80.82%
        '''
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        count = 0
        while head:
            count += 1
            if count == 1:
                cur1 = head
                head = head.next
            else:
                cur1.next = head.next
                pre.next = head
                head.next = cur1
                head = cur1.next
                pre = cur1
                count = 0
        return dummy.next

    def swapPairs_2(self, head):
        '''
        To be more concise and less care about the order of swap. We
        can just swap then all at once.
        From pre -> a -> b -> b.next to pre -> b -> a -> b.next
        '''
        pre = dummy = ListNode(0)
        dummy.next = head 
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next

    def swapPairs_3(self, head):
        '''
        Same idea, but recursive way.
        '''
        if not head or not head.next:
            return head
        temp = head.next
        head.next, temp.next = self.swapPairs_3(temp.next), head
        return temp 

####### rotate list #######
    def rotateRight(self, head, k):
        '''
        Given a list, rotate the list to the right by k places,
        where k is non-negative
        1-2-3-4-5, k=2 -> 4-5-1-2-3
        Note that k could be larger than the length of the list.

        The idea is to go over the list, keep track of the last k node.
        If k is larger than the list len, use mod operation to find the
        least number needed to rotate right, and then do the iteration
        from the start again.

        This one achieves 100% performance.
        '''
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p1 = p2 = 0
        while head.next:
            p2 += 1
            if p2-p1 == k:
                pre = pre.next
                p1 += 1
            head = head.next
        if not p1:
            k = k%(p2+1)
            head = dummy.next
            p1 = p2 = 0
            while head.next:
                p2 += 1
                if p2-p1 == k:
                    pre = pre.next
                    p1 += 1
                head = head.next
        if p1:
            head.next = dummy.next
            dummy.next = pre.next
            pre.next = None
        return dummy.next
    
    def rotateRight_2(self, head, k):
        '''
        Same idea but make the code more simplified by adding a helper function
        that can be used twice.
        '''
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        p1, p2, pre, head = self.rotate_helper(head, k, pre)
        if not p1:
            p1, p2, pre, head = self.rotate_helper(dummy.next, k%(p2+1), pre)
        if p1:
            head.next = dummy.next
            dummy.next = pre.next
            pre.next = None
        return dummy.next
    
    def rotate_helper(self, head, k, pre):
        p1 = p2 = 0
        while head.next:
            p2 += 1
            if p2-p1 == k:
                pre = pre.next
                p1 += 1
            head = head.next
        return (p1, p2, pre, head)
    
    def rotateRight_3(self, head, k):
        '''
        From the other discussions. The idea is the same, first count the length
        of the list, connect the tail to the head. Then break the n-k node. Could
        get rid of the dummy node though. This saves a lot of coding, but not as
        fast as the previous code.
        '''
        if not head:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n +=1
        tail.next = head
        for i in range(n-k%n):
            tail = tail.next
        ans = tail.next
        tail.next = None
        return ans
        
####### Remove duplicates from sorted list #######
    def deleteDuplicates(self, head):
        '''Given a sorted linked list, deleted all duplicates sun that each
        element appear only once.

        46 ms, 100%
        '''
        if not head:
            return head
        ans = head
        slow = head
        while head.next:
            head = head.next
            if slow.val != head.val:
                slow.next = head
                slow = slow.next
        slow.next = None
        return ans
    def deleteDuplicates_2(self, head):
        '''
        The previous code can be simplified to be more concise and use less
        variables and code.
        '''
        current = head
        ## The current just check for the case when head == None
        ## Or just use a if statement at the beginning
        while current and current.next:
            if current.val == current.next.val:
                ## using this line could save the code to append None in the end
                current.next = current.next.next
            else:
                current = current.next
        return head
    def deleteDuplicates_3(self, head):
        '''
        Could use recursion to save code.
        '''
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates_3(head.next)
        return head.next if head.val == head.next.val else head
    
####### Delete duplicates from sorted list #######
    def deleteDuplicates_all(self, head):
        '''
        Follow up the previous question of removing duplicates, now we want
        to delete all duplicate numbers, only leaving distinct numbers from
        the list.

        The idea is that a node will be append to ans only when it does not
        match previous element and next element. Be aware of the corner cases,
        especially the endding node.
        
        55 ms, 84.58%.
        '''
        if not head or not head.next:
            return head
        ref = ListNode(None)
        dummy = ListNode(0)
        ans = dummy
        while head.next:
            if head.val != ref.val and head.val != head.next.val:
                ans.next = head
                ans = ans.next
            ref = head
            head= head.next
        if head and head.val != ref.val:
            ans.next = head
        else:
            ans.next = None
        return dummy.next
    def deleteDuplicates_all_2(self, head):
        '''
        The idea is to use while loop to skip all the duplicates, then
        append the new node to the end. In each iteration, it checks whether
        the node is duplicated by the following node, but it will decide to
        append it to ans until next iteration.
        
        '''
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            ## brilliant if statement here, it append assign cur.next
            ## pre.next as the candidate, and check if this candidate is
            ## duplicated in the next iteraction. If not, formally move on
            ## with the pre = pre.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next
    
    def deleteDuplicates_all_3(self, head):
        '''
        A recursive solution.
        '''
        if not head:
            return head
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates_all_3(head.next)
        else:
            head.next = self.deleteDuplicates_all_3(head.next)
        return head

######### partitioin list #########
    def partition(self, head, x):
        '''
        Given a linked list and a value x, partition it such that all nodes
        less than x come before nodes greater than or equal to x.
        Preserve the original relative order.

        The idea is to build two lists separately and combined them together
        in the end. Be aware to append None to the last node.
        42 ms, 87.77%
        '''
        l1 = dummy1 = ListNode(0)
        l2 = dummy2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = dummy2.next
        return dummy1.next
    
######### reverse linked list #########
    def reverseList(self, head):
        '''Reverse a singly linked list.

        The idea is that at each step, link back to previous node. Need to 
        use extra memory to first save the next node before relink.
        Time complexity O(n), space complexity O(1)
        45 ms, 89.11%
        '''
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
    def reverseList_2(self, head):
        '''
        The same idea with previous one but in a recursive way.
        '''
        if not head:
            return head
        temp = self.reverseList(head)
        head.next = None
        return temp
    def reverse_helper(self, head):
        if head and head.next:
            temp = head.next
            head.next.next = head
            return self.reserse_helper(temp)
        return head
    def reverseList_3(self, head):
        '''
        Simplified recursion using back tracking. Each step links back and
        breaks a link.
        Time complexity O(n), space complexity O(n) comes from implicit 
        stack space due to recursion.
        '''
        if not head or not head.next:
            return head
        temp = self.reverseList_3(head.next)
        head.next.next = head
        head.next = None
        return temp

######### reverse linked list ii #########
    def reverseBetween(self, head, m, n):
        '''Reverse a linked list from position m to n. 
        Do it in-place and in one-pass.
        Assume position (starts from 1): 1 <= m <= n <= length of list

        The idea to reverse is the same as the previous code. Just added
        some code select the starting and ending position. Not very concise
        to handle the corner cases.
        35 ms, 94.54%
        '''
        dummy = ListNode(None)
        dummy.next = head
        count = 1
        while count < m:
            dummy = dummy.next
            count += 1
        top = dummy
        tail  = top.next
        if count == m:
            pre = dummy.next
            dummy = dummy.next.next
            count += 2
        while count <= n+1:
            temp = dummy.next
            dummy.next = pre
            pre = dummy
            dummy = temp
            count += 1
        tail.next = dummy
        top.next = pre
        if m == 1:
            return top.next
        else:
            return head
    def reverseBetween_2(self, head, m, n):
        '''
        Uses for loop and clean up the code a bit.
        The idea is the same, but the key point here is to assign 
        reverse == none, which acts as pre in previous code, where I initialized
        it to be a node when count == m. But this is acutally not neccessary, as
        long as we reassign a node to reverse, it will be fine. What following 
        code did is first assign pre as None, and at last, cut the link to none
        and point to the tail of the list. This saves all the code I have for 
        the corner cases in previous code.
        '''
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        reverse = None
        cur = pre.next
        for i in range(n-m+1):
            temp = cur.next
            cur.next = reverse
            reverse = cur
            cur = temp
        pre.next.next = cur
        pre.next = reverse
        return dummy.next

######### testing #########
mysol = sol()

## add two numbers
#nums1 = [2,4,3]
#nums2 = [5,6,4]
#print mysol.addTwoNumbers_2(cast_list(nums1), cast_list(nums2))

## remove nth from the end
#nums = range(3)
#print nums
#print mysol.removeNthFromEnd_3(cast_list(nums), 2)

## merge two lists
#nums1 = [1, 3, 6]
#nums2 = [2, 3, 5, 8]
#print mysol.mergeTwoLists(cast_list(nums1), cast_list(nums2))

## merge k lists
#nums = [ range(1, i) for i in range(3, 8)]
#nums = [[1,3,5], [2,4,6],[1,2,6]]
#nums = [[0,2,4], []]
#nums = [[]]
#for item in map(cast_list, nums):
#    print item
#print nums
#print 'merged as'
#print mysol.mergeKLists_3(map(cast_list, nums))

## swap nodes in pairs
#nums = range(6)
#print mysol.swapPairs_3(cast_list(nums))

## rotate list
##nums = range(5)
##k = 5
##print mysol.rotateRight_3(cast_list(nums), k)

## Remove duplicates
##import random
##nums = sorted([random.randint(0, 5) for _ in range(10)])
##print nums
##print mysol.deleteDuplicates(cast_list(nums))
##print mysol.deleteDuplicates_2(cast_list(nums))
##print mysol.deleteDuplicates_3(cast_list(nums))

## Delete duplicates
##import random
##nums = sorted([random.randint(0, 5) for _ in range(10)])
##print nums
##print mysol.deleteDuplicates_all(cast_list(nums))
##print mysol.deleteDuplicates_all_2(cast_list(nums))
##print mysol.deleteDuplicates_all_3(cast_list(nums))

## Partition list
##import random
##nums = sorted([random.randint(0, 5) for _ in range(10)])
##x = 3
##print nums
##print mysol.partition(cast_list(nums), x)

## Reverse list
##nums = range(5)
##print mysol.reverseList(cast_list(nums))
##print mysol.reverseList_2(cast_list(nums))

## Reverse list II
nums = range(10)
print nums
print mysol.reverseBetween(cast_list(nums), 1, 2)
print mysol.reverseBetween_2(cast_list(nums), 2, 2)
