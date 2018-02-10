#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.
class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.mydict = {}
        ## the following may contain collisions use put() instead
        ##for item in pairs:
        ##    self.mydict[item[0]] = [item[1]]
        ##for item in pairs:
        ##    self.put(itemp[0], item[1])

    # Associates the value v with the key k.
    def put(self, k, v):
        if k in self.mydict:
            self.mydict[k].append(v)
        else:
            self.mydict[k] = [v]
    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.
    def get(self, k):
        return self.mydict.get(k, [])

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)
def subsequenceHashes(seq, k):
    cur = ''
    while len(cur) < k:
        cur += seq.next()
    cur_hash = RollingHash(cur)
    yield cur, cur_hash.current_hash()
    while True:
        try:
            pre = cur[0]
            nex = seq.next()
            cur = cur[1:]+nex
            yield cur, cur_hash.slide(pre, nex)
        except StopIteration:
            break
    ## the following code from solution is more neat
    ## this one also return the postion
    ##try:
    ##    assert k > 0
    ##    subseq = ''
    ##    for i in range(k):
    ##        subseq += seq.next()
    ##    rh = RollingHash(subseq)
    ##    pos = 0
    ##    while True:
    ##        yield (rh.current_hash(), (pos, subseq))
    ##        pre = subseq[0]
    ##        subseq = subseq[1:]+seq.next()
    ##        rh.slide(pre, subseq[-1])
    ##        pos += 1
    ##except StopIteration:
    ##    return


# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)
def intervalSubsequenceHashes(seq, k, m):
##    cur = ''
##    while len(cur) < k:
##        cur += seq.next()
##    cur_hash = RollingHash(cur)
##    yield cur, cur_hash.current_hash()
##    count = 0
##    while True:
##        count += 1
##        try:
##            pre = cur[0]
##            nex = seq.next()
##            cur = cur[1:]+nex
##            if count == m:
##                yield cur, cur_hash.slide(pre, nex)
##                count = 0
##            else:
##                cur_hash.slide(pre, nex)
##        except StopIteration:
##            break
    ## more concise solution:
    assert m >= k
    try:
        pos = 0
        while True:
            subseq = ''
            for i in range(0, k):
                subseq += seq.next()
            rh = RollingHash(subseq)
            yield (rh.hash(), (pos, subseq))
            for i in range(0, m-k):
                seq.next()
            pos += m
    except StopIteration:
        return


# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k, m):
    ## could just use the generator to cast items in the dictionary
    adict = Multidict(intervalSubsequenceHashes(a, k, m))
##    for i, item in enumerate(intervalSubsequenceHashes(a, k, m)):
##        adict.put(item[1], (i*m, item[0]))
    for hashval, (bpos, bsubseq) in subsequenceHashes(b, k):                                               
        for apos, asubseq in adict.get(hashval):
            if asubseq == bsubseq:
            	yield (apos, bpos)
    return
##    for i, item in enumerate(subsequenceHashes(b, k)):
##        for match in adict.get(item[1]):
##            if item[0] == match[1]:
##                yield  match[0], i
        

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500,500), sys.argv[1], sys.argv[2], 8, 100)
