class Solution(object):
    def NaiveSearch(self, pat, text):
        '''Naive pattern searching, time complexity O(m(n-m+1))

        :type pat: str
        :type text: str
        :rtype: int
        '''
        if len(pat) > len(text):
            return 0
        count = 0
        for shift in range(len(text)-len(pat)+1):
            for i in range(len(pat)):
                if pat[i] != text[i+shift]:
                    break
                if i == len(pat)-1:
                    print 'Pattern found at index starting at', shift
                    count += 1
        return count

    def KMPSearch(self, pat, text):
        '''The previous naive search algorithm could be improved by 
        skipping strings in pattern that already matches.
        This reduce the time complexity to O(n).
        
        The idea is to get the index list of the pattern list,
        where the longest matching prefix and suffix is stored. In
        other words, the charaters that can be skipped when the pointer
        move to that element in the pattern list.
        '''
        if len(pat) > len(text):
            print 'No pattern found'
            return 0
        lps = self.calcLPS(pat)
        i = 0
        j = 0
        count = 0
        while i < len(text):
            if text[i] == pat[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == len(pat):
                j = lps[j-1]
                print 'Pattern found at index starting at', i-len(pat)
                count += 1
        return count

    def calcLPS(self, pat):
        '''
        The idea is to keep moving forward both pointers, if the element matches
        with the reference element. When a dismatch is found, move back the refence
        pointer, until a match is found, or the pointer reaches the beginning of 
        the pattern, in which case the element pointer move forward again. 05-05-17

        The previous idea is wrong, because we could not immediately increase the 
        element pointer once we found a match. A element pointer will be increased
        only when all of previous elements have been matched or when the pointer 
        reaches the beginning of the pattern.
        For example: if we have a pattern of abcabcb, the previous function will
        give 0001232. The last digit is wrong because it only examined 1 char.

        Instead, we use a similar way as we did in search, let j = lps[j-1]. The idea
        is to use the lps we've already built to skip duplicated comparisons.
        Take abcabcabcb as an example, which will out put 0001234560.
        When determine the last char, we have ref pointer j at 7 and element pinter at
        last digit. Since we know the lps[6], so we don't have to campare from the 
        beginning, but just jump to lps[6]. Then if lps[6] matches with pat[i], then
        we've found the lps[i], and move i and i forward. If not, repeat this process
        until a match is found or the ref pointer reaches the beginning of the pattern.

        :rtype: list
        '''
        j = 0
        lps = [0 for _ in pat]
        i = 1
        while i < len(pat):
            if pat[i] == pat[j]:
                lps[i] = j+1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return lps

    def RKSearch(self, pat, text, base = 256, prime = 101):
        '''
        Instead of using sophiscated algorithms to skip matched strings, the Rabin-
        Karp algorithm instead focus on speeding up the comparison process. This could
        be achieved by hashing pattern string and window string with same size in text.

        The key is to choose a hash function that could well represent the string, and 
        each hashing value could be linked to previous hashing value with O(1) manipulation.
        This could be achieved by rolling hashing.

        Rabin fingerprint:
        Given a string a1a2...ak, we represent it as summation[1 -> i](ai*b**i), where b is
        a base chosen to be larger than the number of characters (usually 256). Since this
        may result huge interger, the remainder mod large prime number is usually calculated.
        Multiplication method:
        The previous hash function is limited by the speed of mod calculation, thus cannot
        compute hash functions quickly. So we can replace the modulus with something like 
        2**32 and replace th abse with some small prime. 37 is based on folklore, and 97, 31
        also has supporters. Almost medium-sized prime would work.
        '''
        if len(pat) > len(text):
            return 0
        hp = 0
        ht = 0
        rn = 1
        count = 0
        for i in range(len(pat)-1):
            rn = (rn*base)%prime    # compute the remainder of b**(len(pat)-1)
        for i in range(len(pat)):
            hp = (hp*base+ord(pat[i]))%prime
            ht = (ht*base+ord(text[i]))%prime
        for i in range(len(text)-len(pat)+1):
            if hp == ht:
                for j in range(len(pat)):
                    if pat[j] != text[i+j]:
                        break
                if j == len(pat)-1:
                    count += 1
                    print 'Pattern found at index starting at', i
            if i < len(text)-len(pat):
                ht = ((ht-ord(text[i])*rn)*base+ord(text[i+len(pat)]))%prime
                if ht < 0:
                    ht += prime
        return count

    def hashSearch(self, pat, text, base = 37):
        '''
        This function used the Multiplication method mentioned previously.
        In C, if a number overflows, it will be automatically truncated,  which
        is equal to mod 2**32
        '''
        if len(pat) > len(text):
            return 0
        count = 0
        hp = 0
        ht = 0
        rn = 1
        for i in range(len(pat)-1):
            rn *= base
        for i in range(len(pat)):
            hp = hp*base+ord(pat[i])
            ht = ht*base+ord(text[i])
        for i in range(len(text)-len(pat)+1):
            if hp == ht:
                for j in range(len(pat)):
                    if pat[j] != text[i+j]:
                        break
                if j == len(pat)-1:
                    count += 1
                    print 'Pattern found at index starting at', i
            if i < len(text)-len(pat):
                ht = (ht-ord(text[i])*rn)*base+ord(text[i+len(pat)])
        return count

    def FASearch(self, pat, text):
        '''
        This function uses finite automata based pattern searching algorithm.
        First, we need to construct a 2D array that represents the finit automata
        of pattern. At each state, each charactor has its corresponding next state. 
        The search algorithm starts with state 0 and text[0], and look for next 
        state. If the state reaches final state, then a pattern is found.
        Here 2 ways of constructing FA table are included.
        '''
        fa1 = self.NaiveState(pat)
        fa2 = self.KMPState(pat)
        if fa1 == fa2:
            fa = fa2
        else:
            return 'Something wrong with FA table'
        count = 0
        state = 0
        for ind, i in enumerate(text):
            state = fa[state][ord(i)]
            if state == len(pat):
                count += 1
                print 'Pattern found at index starting at', ind-len(pat)+1
        return count

    def NaiveState(self, pat, noc = 256):
        '''
        This function uses naive way to define the next state of current character.
        If current character is the same as next character in pattern, increase the
        state. Otherwise, check the longest prefix strings matches the suffix string.
        (The process could be optimized using KMP algorithm)
        '''
        fa = [[0 for i in range(noc)] for _ in range(len(pat)+1)]
        for state in range(len(fa)):
            for char in range(noc):
                if state < len(pat) and char == ord(pat[state]):
                    fa[state][char] = state+1
                else:
                    length = state-1
                    while length >= 0:
                        if char == ord(pat[length]):
                            count = 0
                            for i in range(length):
                                if pat[i] != pat[state-length+i]:
                                    break
                                else:
                                    count += 1
                            if count == length:
                            # instead of using i == length-1
                            # where length equals to 0 or 1 will cause problem 
                                fa[state][char] = length+1
                                break 
                        length -= 1
        return fa
    def KMPState(self, pat, noc = 256):
        '''
        Using  similar strategy to KMP algorithm, this function constructs FA by
        recording the lps of each state. At each state, assign state+1 to char that
        matches the pattern. The lps is accessed by lps row and pat[i].
        '''
        fa = [[0 for _ in range(noc)]]
        fa[0][ord(pat[0])] = 1
        lps = 0
        for i in range(1, len(pat)):
            fa.append(fa[lps][:])
            fa[i][ord(pat[i])] = i+1
            lps = fa[lps][ord(pat[i])]
        fa.append(fa[lps][:])
        return fa
    def BadCharSearch(self, pat, text, noc = 256):
        '''
        This function use bad character heuristic to shift pattern over text by more
        than a one.
        The bad character means the character in text that does not match with current
        character in pattern. Whenever a dismatch is found, we move the pattern to the
        last occurence of that character in pattern. If the character is not found in 
        pattern, we just shift the whole pattern by len(pat). Notice that we can only
        move forward, so shift at least 1 char.
        A list with the size of the number of all characters is needed to store the 
        last occurence of the chars in pattern.
        '''
        if len(pat) > len(text):
            return 0
        badchar = [0]*noc
        for ind, i in enumerate(pat):
            badchar[ord(i)] = ind
            j = len(pat)-1
        shift = 0
        count = 0
        while shift <= len(text)-len(pat):
            j = len(pat)-1
            while j >= 0 and pat[j] == text[shift+j]:
                j -= 1
            if j < 0:
                print 'Pattern found at index starting at', shift
                count += 1
                if shift+len(pat) < len(text):
                # check if text has reached the end
                    shift += len(pat)-badchar[ord(text[shift+len(pat)])]
                else:
                    break
            else:
                shift += max(1, j-badchar[ord(text[shift+j])])
        return count

    def SuffixTreeSearch(self, pat, text):
        '''
        Using suffix trie method to build a trie for text and then search
        pattern in the trie. The building of trie may be costly, but the
        seach algorithm is only O(len(pat)). So this method is usually for
        a string that does not change a lot.
        Since this involves with the knowledge of data structure, I will 
        just leave it here, and finish when I've cover that part of knowledge.
        '''
        return 0
mysol = Solution()
pat = 'AABAA'
text = 'AABAACAADAABAAABAABAA'
print mysol.NaiveSearch(pat, text)
print mysol.KMPSearch(pat, text)
print mysol.RKSearch(pat, text)
print mysol.hashSearch(pat, text)
print mysol.FASearch(pat, text)
print mysol.BadCharSearch(pat, text)


#fa = mysol.NaiveState(pat)
#for i in fa:
#    print [i[item] for item in [ord('A'), ord('C'), ord('G')]]
#print ''
#fa = mysol.KMPState(pat)
#for i in fa:
#    print [i[item] for item in [ord('A'), ord('C'), ord('G')]]
