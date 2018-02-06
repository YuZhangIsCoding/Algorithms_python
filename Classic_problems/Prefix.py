class sol(object):
    def longestCommonPrefix(self, strs):
        '''
        Write a function to find the longest common prefix string amongst
        an array of strings.
        The idea is compare the prefix character by character, and is so-called
        vetical scanning.

        46 ms, 72.34%
        '''
        if strs == []:
            return ''
        elif len(strs) == 1:
            return strs[0]
        for i, item in enumerate(strs[0]):
            for strings in strs[1:]:
                if len(strings) == i or strings[i] != item:
                    return strs[0][:i]
        return strs[0]
    def longestCommonPrefix_2(self, strs):
        '''
        Here present the horizontal screening. Iterate through strs, in each 
        iteration, find the longest common prefix.
        '''
        if strs == []:
            return ''
        lcp = strs[0]
        for item in strs[1:]:
            while lcp and lcp != item[:len(lcp)]:
                lcp = lcp[:-1]
            return lcp
        return lcp

    def longestCommonPrefix_3(self, strs):
        '''
        Divide and conquer. The idea is that the common prefix can be determined
        by comparing the common prefixes of 2 sub-lists. And the common prefix of
        sub-lists can be obtained using recursive way until the sub-list only 
        contain 1 string.
        '''
        return self.recursion(0, len(strs)-1, strs)
    def recursion(self,left, right, strs):
        if left == right:
            return strs[left]
        mid = left+(right-left)/2
        lcpleft = self.recursion(left, mid, strs)
        lcpright = self.recursion(mid+1, right, strs)
        return self.compare_lcp(lcpleft, lcpright)
    def compare_lcp(self, s1, s2):
        n = min(len(s1), len(s2))
        for i in range(n):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:n]

    def longestCommonPrefix_4(self, strs):
        '''
        Uses binary search method.
        '''
        if strs == []:
            return ''
        high = min([len(item) for item in strs])
        low = 1
        while low <= high:
            mid = low+(high-low)/2
            if self.iscommon(strs, mid):
                low = mid+1
            else:
                high = mid-1
        return strs[0][:(low+(high-low)/2)]
    def iscommon(self, strs, mid):
        s = strs[:mid]
        n = len(s)
        for item in strs[1:]:
            if s != item[:n]:
                return False
        return True

    def longestCommonPrefix_5(self, strs):
        '''
        Implement trie. Requires knowledge about trie.
        '''
        return

mysol = sol()
strs = ['12344531', '12340929348', '1234']
#print mysol.longestCommonPrefix(strs)
#print mysol.longestCommonPrefix_3(strs)
print mysol.longestCommonPrefix_4(strs)
