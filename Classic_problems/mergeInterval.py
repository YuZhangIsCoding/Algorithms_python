import operator
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Sol(object):
    def mergeInterval(self, intervals):
        if intervals == []:
            return []
        intervals = sorted(intervals, key = operator.attrgetter('start'))
        ans = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            if temp.end < intervals[i].start:
                ans.append(temp)
                temp = intervals[i]
            else:
                temp = Interval(temp.start, max(temp.end, intervals[i].end))
        ans.append(temp)
        return ans
    def mergeInterval_2(self, intervals):
        '''
        Instead of attrgetter, we could just use lambda function.
        '''
        ans = []
        for i in sorted(intervals, key = lambda i: i.start):
            if ans and i.start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)
        return ans

a = [Interval(i, j) for i in range(3) for j in range(5)]
#import operator
#b = sorted(a, key = operator.attrgetter('end'))
intervals = [Interval(i[0], i[1]) for i in [[2,3],[4,5],[6,7],[8,9],[1,10]]]
print [[i.start, i.end] for i in intervals]
mysol = Sol()
intervals = mysol.mergeInterval(intervals)
print [[i.start, i.end] for i in intervals]
