class TreeNode(object):
    '''Definition for a binary tree node'''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

class BSTNode(TreeNode):
    '''Binary search tree'''
    def insert(self, node):
        '''Insert a node in the tree, if the value is smaller than current
        node, go to the left branch. Otherwise, go to the right.
        '''
        if node.val < self.val:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)

class sol(object):
    def isSameTree(self, p, q):
        '''Given two binary trees, write a function to check if they are equal.
        Two binary trees are considered equal if they are structurally identical
        and the nodes have the same value.

        The idea is to use recursion. Three cases:
        case 1: both of them are NIL return True
        case 2: one of them is NIL return False
        case 3: neither of them is NIL and the value equals, recurse on their childs
        
        32 ms, 82%
        '''
        if (not p and q) or (not q and p):
            return False
        elif not p and not q:
            return True
        else:
            if p.val == q.val and self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right):
                return True
            else:
                return False
    def isSameTree_2(self, p, q):
        '''Same idea with previous one, but some tricks can used to reduce the code.
        The use of p is q contains both case 1 and case 2.
        This function can further reduced to one line by returning p and q ... or p is q 
        '''
        if p and q:
            return p.val == q and self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
        return p is q

    def numTrees(self, n):
        '''Given n, how many structurally unique BST's that store values 1...n?

        The idea is to divide the tree into 2 sub trees, and sum up all the
        possible combinations.
        39 ms, 33.02%
        32 ms, 72.04%
        '''
        mydict = {0: 1, 1: 1}
        for item in range(2, n+1):
            sum = 0
            for i in range(item):
                sum += mydict[i]*mydict[item-i-1]
            mydict[item] = sum
        return mydict[n]
        ##list version
        ##mylist = [1, 1]
        ##for item in range(2, n+1):
        ##    mylist.append(0)
        ##    for i in range(item):
        ##        mylist[-1] += mylist[i]*mylist[item-i-1]
        ##return mylist[-1]
    def numTrees_2(self, n):
        '''This is also known as catalan numbers in math:
        Cn = 1/(n+1)Combination(2n, n)
        '''
        ans = 1
        for i in range(1, n+1):
            # careful for the *=
            ans = ans*(i+n)/i
        return ans/(n+1)

    def generateTrees(self, n):
        '''Following previous problem, generate all structurally unique
        BST that stores 1...n.
        Return a list of nodes.

        The idea is to use divide and conquer method. In the origianl list,
        pick a node as the current root element and divide the list into two
        parts. The left part must be in root's left children and right part
        must be root's right children. In each sublist repeat the process.
        Return a list of possible roots back.
        98 ms, 35.48%
        85 ms, 66.94%
        '''
##        ans = []
##        for item in range(n):
##            ans.extend(self.gen_rec(range(1, n+1), item))
##        return ans
        return self.gen_rec_2(1, n)
    def gen_rec(self, mylist, n):
        '''This one works for all sorted list'''
        if not mylist or n == -1:
            return [None]
        if len(mylist) == 1:
            return [TreeNode(mylist[0])]
        ans = []
        ## need to solve the case when the root is at the edges
        for left in xrange(n) or [-1]:
            for right in xrange(n+1, len(mylist)) or [-1]:
                leftchild = self.gen_rec(mylist[:n], left)
                rightchild = self.gen_rec(mylist[n+1:], right-n-1)
                for l in leftchild:
                    for r in rightchild:
                        root = TreeNode(mylist[n])
                        root.left = l
                        root.right = r
                        ans.append(root)
        return ans
    def gen_rec_2(self, start, end):
        '''Same idea, but because we are just dealing with consequetive numbers,
        we can use start and end pointer to avoid passing lists and may save
        same time.

        86 ms, 65%
        '''
        ## this two lines can be replaced by the or condition at bottom
##        if start > end:
##            return [None]
        ans = []
        for i in xrange(start, end+1):
            leftchild = self.gen_rec_2(start, i-1)
            rightchild = self.gen_rec_2(i+1, end)
            for l in leftchild:
                for r in rightchild:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans or [None]

    def inorderTraversal(self, root):
        '''Given a binary tree, return the inorder traversal of its nodes' val.
        [1, null, 2, 3] return [1, 3, 2].
        Note recursive solution is trivial, could you do it iteratively.

        Inorder traversal means traversing the values by the order of
        (left, root, right).

        Recursive way: go to the left child if the root has one, append current
        root val to path, and go to the right child if the root has one.

        32 ms, 86.75%
        '''
        if not root:
            return []
        path = []
        self.iotravel_rec(root, path)
        return path
    
    def iotravel_rec(self, root, path):
        if root.left:
            self.iotravel_rec(root.left, path)
        path.append(root.val)
        if root.right:
            self.iotravel_rec(root.right, path)

    def inorderTraversal_2(self, root):
        '''Iterative way
        The idea is to keep track of the path and status of whether a node is
        visited.

        35 ms, 72.54%
        32 ms, 86.75%
        '''
        if not root:
            return []
        path = [root]
        status = [1]
        ans = []
        while path:
            current = path[-1]
            while current.left and status[-1]:
                status[-1] = 0
                current = current.left
                path.append(current)
                status.append(1)
            ans.append(path.pop().val)
            status.pop()
            if current.right:
                path.append(current.right)
                status.append(1)
        return ans
    def inorderTraversal_3(self, root):
        '''Iterative way
        The idea is to keep track of the path if the left child is None, pop
        that node and append the node's val, and start on the right child of
        the node (if there's any).
        '''
        path = []
        ans = []
        while root or path:
            while root:
                path.append(root)
                root = root.left
            root = path.pop()
            ans.append(root.val)
            root = root.right
        return ans
    def levelOrder(self, root):
        '''Given a binary tree, return the level order traversal of its nodes'
        values. (ie, from left to right, level by level)
        Return a list of lists of the values at each level

        Use 2 lists to record current nodes and next nodes.
        48 ms, 64.79%
        49 ms, 51.83%
        '''
        if not root:
            return []
        ans = [[]]
        cur = [root]
        pnext = []
        while cur or pnext:
            node = cur.pop(0)
            ans[-1].append(node.val)
            if node.left:
                pnext.append(node.left)
            if node.right:
                pnext.append(node.right)
            if not cur and pnext:
                ans.append([])
                cur = pnext[:]
                pnext = []
        return ans
    def levelOrder(self, root):
        '''Actually the cur.pop(0) will take O(len(list)). So this does no good
        to reduce the time
        59 ms, 18.91%
        39 ms, 98.86%
        49 ms, 51.83%
        '''
        if not root:
            return []
        ans = []
        cur = [root]
        while cur:
            temp = []
            pnext = []
            for item in cur:
                temp.append(item.val)
                if item.left:
                    pnext.append(item.left)
                if item.right:
                    pnext.append(item.right)
            ans.append(temp)
            cur = pnext
        return ans
    def levelOrder_3(self, root):
        '''Recursive way. Use addition variable depth to indicate the level.

        45 ms, 77.67%
        59 ms, 18.91%
        '''
        ans = []
        self.levelOrder_rec(root, 0, ans)
        return ans
    def levelOrder_rec(self, root, depth, ans):
        if not root:
            return
        if len(ans) == depth:
            ans.append([])
        ans[depth].append(root.val)
        self.levelOrder_rec(root.left, depth+1, ans)
        self.levelOrder_rec(root.right, depth+1, ans)
        return
    def zigzagLevelOrder(self, root):
        '''Following up the previous problem, return the zigzag level order
        traversal of its nodes' values. (ie, from left right and then from
        right to left).
        Return a list of lists of node values

        39 ms, 75.49%
        55 ms, 15.25%
        42 ms, 56.20%
        '''
        if not root:
            return []
        ans = [[]]
        cur = [root]
        pnext = []
        level = 0
        while cur or pnext:
            node = cur.pop()
            if level%2 == 0:
                if node.left:
                    pnext.append(node.left)
                if node.right:
                    pnext.append(node.right)
            else:
                if node.right:
                    pnext.append(node.right)
                if node.left:
                    pnext.append(node.left)
            ans[-1].append(node.val)
            if not cur and pnext:
                level += 1
                ans.append([])
                cur = pnext[:]
                pnext = []
        return ans
    def zigzagLevelOrder_2(self, root):
        '''
        Same idea as levelorder_2, but iterate reversely each time.
        39 ms, 75.49%
        42 ms, 56.20%
        '''
        if not root:
            return []
        ans = []
        cur = [root]
        level = True
        while cur:
            temp = []
            pnext = []
            for node in cur[::-1]:
                temp.append(node.val)
                if level:
                    if node.left:
                        pnext.append(node.left)
                    if node.right:
                        pnext.append(node.right)
                else:
                    if node.right:
                        pnext.append(node.right)
                    if node.left:
                        pnext.append(node.left)
            ans.append(temp)
            cur = pnext
            level = not level
        return ans

    def zigzagLevelOrder_3(self, root):
        '''Recursive DFS. The performance is poor because insert is used.
        if we use a single-linked list, the speed may be increase because
        insertion in initial position takes O(1) then.
        '''
        ans = []
        self.zigzaglevelorder_rec(root, ans, 0)
        return ans
    def zigzaglevelorder_rec(self, root, ans, depth):
        if not root:
            return
        if len(ans) == depth:
            ans.append([])
        if depth%2 == 0:
            ans[depth].append(root.val)
        else:
            ans[depth].insert(0, root.val)
        self.zigzaglevelorder_rec(root.left, ans, depth+1)
        self.zigzaglevelorder_rec(root.right, ans, depth+1)
        return
        

    def isValidBST(self, root):
        '''Given a binary tree, determine if it is a valid binary search
        tree (BST).

        The idea is to set a left bound and right bound, every time a left
        child is checked, passes a right bound because all the left children
        cannot be larger than the root. And every time a right child is checked
        passes a left bound.
        82 ms, 30.87%
        62 ms, 88.74%
        69 ms, 67.84%
        '''
        if not root:
            return True
        return self.isValid_rec_2(root, None, None)
        return True
    def isValid_rec(self, root, left, right):
        ## 2 failing cases: left is larger than root
        ## left is smaller than left bound
        ## do the 2 check above recursively
        if root.left:
            if root.left.val >= root.val or\
               (left and root.left.val <= left.val) or\
               not self.isValid_rec(root.left, left, root):
                return False
        if root.right:
            if root.right.val <= root.val or\
               (right and root.right.val >= right.val) or\
               not self.isValid_rec(root.right, root, right):
                return False
        return True
    def isValid_rec_2(self, root, left, right):
        ''' The idea is the same, but we can further simply the 2 failing cases
        as 1 case, that a node must within the left bound and right bound.
        65 ms, 83.15%
        
        '''
        if not root:
            return True
        if (left and root.val <= left.val) or (right and root.val >= right.val):
            return False
        return self.isValid_rec_2(root.left, left, root) and \
               self.isValid_rec_2(root.right, root, right)

    def isSymmetric(self, root):
        '''Given a binary tree, check whether it is a mirror of itself.
        Bonus point if do it recursively and iteratively.

        Recursively, check the node has the same values and recursion on their
        children.

        46 ms 42.25%'''
        if not root:
            return True
        return self.isSym_rec(root.left, root.right)
    def isSym_rec(self, left, right):
        if left is None and right is None:
            return True
        if left and right:
            if left.val != right.val:
                return False
            return self.isSym_rec(left.left, right.right) and \
                   self.isSym_rec(left.right, right.left)
        return False
    def isSymmetric_2(self, root):
        '''Iteratively

        The idea is to use 2 list to record the nodes from top to bottom
        48ms, 38.01%
        '''
        if not root:
            return True
        lpath = [root.left]
        rpath = [root.right]
        while lpath:
            left = lpath.pop(0)
            right = rpath.pop(0)
            if left and right:
                if left.val != right.val:
                    return False
                lpath.append(left.left)
                lpath.append(left.right)
                rpath.append(right.right)
                rpath.append(right.left)
            elif not left and not right:
                continue
            else:
                return False
        return True
    def isSymmetric_3(self, root):
        '''Same idea as isSymmetric_2, but actually we can achive this use
        only one list
        '''
        path = [root, root]
        while path:
            left = path.pop(0)
            right = path.pop(0)
            if left and right:
                if left.val != right.val:
                    return False
                path.extend([left.left, right.right, left.right, right.left])
            elif not left and not right:
                continue
            else:
                return False
        return True
    def maxDepth(self, root):
        '''Find the maximum depth of a BST.
        The maximum depth is the number of nodes along the longest path from
        the root node down to the farthest leaf node.
        68 ms, 28%
        '''
        return depth_rec(root, 0)
    def depth_rec(root, depth):
        if not root:
            return depth
        depth += 1
        return max(self.depth_rec(root.left, depth), \
                   self.depth_rec(root.right, depth))
    def maxDepth_2(self, root):
        '''
        The previous algorithm could be further reduced as following.
        62 ms, 42.94%
        '''
        if not root:
            return 0
        return max(self.maxDepth_2(root.left), self.maxDepth_2(root.right))+1
    def maxDepth_3(self, root):
        '''
        Iterative way.
        72 ms, 17.83%
        55 ms, 76.14%
        '''
        if not root:
            return 0
        depth = 0
        cur = [root]
        temp = []
        while cur:
            node = cur.pop()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not cur:
                cur = temp
                temp = []
                depth += 1
        return depth
    def buildTree(self, preorder, inorder):
        '''Given preorder and inorder traversal of a tree, construct the binary
        tree.
        Assume no duplicates in the tree.
        '''
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        cur = root
        
####### helper functions #######
    def insert_list(self, mylist):
        if not mylist:
            return None
        root = TreeNode(mylist[0])
        for i in mylist[1:]:
            self.TreeInsert(root, TreeNode(i))
        return root
    def TreeInsert(self, node1, node2):
        if node2.val < node1.val:
            if not node1.left:
                node1.left = node2
            else:
                self.TreeInsert(node1.left, node2)
        else:
            if not node1.right:
                node1.right = node2
            else:
                self.TreeInsert(node1.right, node2)

####### supporting functions #######
def cast_list(mylist):
    root = BSTNode(mylist[0])
    for i in mylist[1:]:
        root.insert(BSTNode(i))
    return root

def build_list(mylist):
    root = BSTNode(mylist[0])
    path = [root]
    cur = [root]
    for i in range(len(mylist)/2):
        node = path.pop(0)
        if mylist[2*i+1] is None:
            node.left = None
        else:
            node.left = BSTNode(mylist[2*i+1])
            if i < len(mylist)/4:
                path.append(node.left)
        if mylist[2*i+2] is None:
            node.right = None
        else:
            node.right = BSTNode(mylist[2*i+1])
            if i < len(mylist)/4:
                path.append(node.right)
    return root


    
####### testing ########
mysol = sol()

## is same tree ##
#import random
#mylist = [random.randint(1,100) for _ in range(10)]
#temp = cast_list(mylist)
#print mysol.isSameTree(temp, temp)

## number of unique BST ##
##print mysol.numTrees_2(10)
##print len(mysol.generateTrees(10))

## inorder traversal ##
##import random
##mylist = [random.randint(1,100) for _ in range(10)]
##temp = cast_list(mylist)
##print sorted(mylist)
##print mysol.inorderTraversal_3(temp)

## Validate BST ##
##import random
##mylist = range(100)
##random.shuffle(mylist)
##mylist = mylist[:10]
##temp = cast_list(mylist)
##print sorted(mylist)
##print mysol.isValidBST(temp)

## symmetric BST ##
##mylist = [1, 2, 2, None, 3, 3, None]
##mylist = [4,-57,-57,None,67,67,None,None,-97,-97]
##temp = build_list(mylist)
##print mysol.isSymmetric(temp)

## level order traversal ##
mylist = [3,9,20,null,null,15,7]
