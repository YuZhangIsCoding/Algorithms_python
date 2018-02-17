def npowermodule(m, n, base, mydict = {}):
    '''O(log(n)) time use divide and conquer
    '''
    if n <= 1:
        mydict[n] = m%base
        return mydict[n]
    if n not in mydict:
        a = npowermodule(m, n//2, base, mydict)
        b = npowermodule(m, n-n//2, base, mydict)
        mydict[n] = (a*b)%base
    return mydict[n]

m = 7
n = 1000
base = 6
print(m**n%base)
print(npowermodule(m, n, base))
