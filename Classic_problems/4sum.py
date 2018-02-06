class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
## 492 ms, 66%
        if len(nums) < 4:
            return []
        out = []
        nums = sorted(nums)
        i = 0
        kref = [len(nums)-1 for _ in nums]
        while i < len(nums)-3 and 4*nums[i] <= target:
            if i > 1 and nums[i] == nums[i-2]:
                i += 1
                continue
            j = i+1
            k = kref[j+1]
            while j < k-1:
                while j < k-3 and nums[j] == nums[j+3]:
                    j += 1
                while j < k-3 and nums[k] == nums[k-3]:
                    k -= 1
                l = j+1
                k = kref[l]
                while l < k:
                    s = nums[i]+nums[j]+nums[k]+nums[l]
                    if s < target:
                        l += 1
                    elif s > target:
                        k -= 1
                        kref[l] = k
                    else:
                        out.append([nums[i], nums[j], nums[l], nums[k]])
                        while l < k and nums[l] == nums[l+1]:
                            l += 1
                        while l < k and nums[k] == nums[k-1]:
                            k -= 1
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while i < k and nums[i] == nums[i+1]:
                            i += 1
                        kref[l] = k
                        l += 1
                        k -= 1
                j += 1
            i += 1
        return out
