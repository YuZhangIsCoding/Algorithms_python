import time
import random
a = random.sample(range(-100000, 100001), 500)
#a = range(-3, 4)
#a += [1]*1000+[0]*10+[2]*10
#a = [1,-2,-5,-4,-3,3,3,5]
target = -11
ts = time.time()
a = sorted(a)
out = []
i = 0
kref = [len(a)-1 for _ in a]
while i < len(a)-3:
    if i > 1 and a[i-2] == a[i-1] and a[i-2] == a[i]:
        i += 1
        continue
    j = i+1
    k = kref[j+1]
    while j < k-1:
        while j < k-3 and a[j] == a[j+1] and a[j] == a[j+2] and a[j] == a[j+3]:
            j += 1
        while j < k-3 and a[k] == a[k-1] and a[k] == a[k-2] and a[k] == a[k-3]:
            k -= 1
        l = j+1
        k = kref[l]
        while l < k:
            s = a[i]+a[j]+a[k]+a[l]
            if s < target:
                l += 1
            elif s > target:
                k -= 1
                kref[l] = k
            else:
                temp = [a[i], a[j], a[l], a[k]]
                out.append(temp)
                while l < k and a[l] == a[l+1]:
                    l += 1
                while l < k and a[k] == a[k-1]:
                    k -= 1
                while j < k and a[j] == a[j+1]:
                    j += 1
                while i < k and a[i] == a[i+1]:
                    i += 1
                kref[l] = k
                l += 1
                k -= 1
        j += 1
    i += 1
#print out
print (time.time()-ts)*100
