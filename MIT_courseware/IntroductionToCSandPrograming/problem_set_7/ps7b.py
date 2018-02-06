import random
def run_sim(test_nums):
    fail = 0
    for i in xrange(test_nums):
        temp = []
        for j in xrange(5):
            temp.append(random.randint(1, 6))
        for j in temp[1:]:
            if temp[0] != j:
                fail += 1
                break
    return 1-fail*1.0/test_nums

print 6*(1.0/6)**5
print run_sim(1000000)
