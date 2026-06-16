class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        counts = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                counts += right - left
                left += 1
            else:
                right -= 1
        return counts
                    
        




             



        
