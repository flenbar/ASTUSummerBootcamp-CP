class Solution(object):
    def minPairSum(self, nums):
        result = []
        left = 0
        right = len(nums)-1
        nums.sort()
        while left < right :
            result.append(nums[left] + nums[right])
            left += 1
            right -= 1
        return max(result)    


        
        
