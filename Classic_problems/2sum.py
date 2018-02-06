class Solution(object):
    def combinationSum(self, candidates, target):
        '''
        Given a collection of candidates, find all unique combinations that 
        sum up to the target number.
        - The same number maybe chosen unlimited number of times.
        - All numbers including target, are positive intergers
        - Must not contain duplicate combinations.
        '''
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)

## quite interesting to know that the list in python could act like pointer in 
## C. When you pass a list to a function, if you modify the elements inside, the
## original list will also change. Following is a test case:
    def inp(self):
        res = [1,2,3]
        self.test(res)
        return res
    def test(self, ans):
        ans[2] = 'Haha'
        return

    def combinationSum2(self, candidates, target):
        '''
        Given a collection of candidates, find all unique combinations that 
        sum up to the target number.
        - Each number may only be used once.
        - All numbers including target, are positive intergers
        - Must not contain duplicate combinations.
        
        Use the same idea but add a condition that skip numbers that is the same 
        as previous number.
        '''
        ans = []
        candidates.sort()
        self.helper(candidates, target, len(candidates)-1, [], ans)
        return ans
    def helper(self, candidates, target, index, path, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(path)
            return
        for i in range(index, -1, -1):
            if i != index and candidates[i] == candidates[i+1]:
                continue
            self.helper(candidates, target-candidates[i], i-1, path+[candidates[i]], ans)

mysol = Solution()
#print mysol.combinationSum([2,3,6,7], 7)
#print mysol.inp()
#print mysol.combinationSum2([10,1,2,7,6,1,5], 8)
#print mysol.combinationSum2([1,1,1,1,2,2,4,6], 10)
print mysol.combinationSum2([1,1,1,3,3,5], 8)

