class Solution(object):
    def pivotArray(self, nums, pivot):
        greater_pivot = []
        less_pivot = []
        pivots = []
        for i in range(len(nums)):
            if nums[i] > pivot :
                greater_pivot.append(nums[i])
            elif nums[i] < pivot :
                less_pivot.append(nums[i]) 
            else:
                pivots.append(nums[i]) 
        result = less_pivot + pivots + greater_pivot
        return result             
                
        
