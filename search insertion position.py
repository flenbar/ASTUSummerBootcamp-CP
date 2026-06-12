class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if target in nums :
                return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
