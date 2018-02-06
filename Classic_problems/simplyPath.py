class Sol(object):
    def simplyPath(self, path):
        '''
        Simplify paths, merge folders, etc
        '''
        coll = path.split('/')
        ans = []
        for i in coll:
            if i == '..':
                if not ans:
                    ans.append(i)
                elif ans[-1] == '..':
                    ans.append(i)
                else:
                    ans.pop()
            elif i == '.' or i == '':
                continue
            else:
                ans.append(i)
        while ans and ans[0] == '..':
            ans.pop(0)
        return '/'+'/'.join(ans)

    def simplyPath_2(self, path):
        '''
        Make it more clean, because the .. need not to be in the path
        '''
        ans = []
        for i in path.split('/'):
            if i == '..':
                if ans:
                    ans.pop()
            elif i and i != '.':
                ans.append(i)
        return '/'+'/'.join(ans)

mysol = Sol()
print mysol.simplyPath("/home//foo/")
print mysol.simplyPath_2("/home//foo/")
