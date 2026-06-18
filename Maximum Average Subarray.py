class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        kth_sum = sum(nums[:k])
        maxi_sum = kth_sum
        left = 0
        for right in range(k, len(nums)):
            kth_sum += nums[right] 
            kth_sum -= nums[left] 
            maxi_sum = max(maxi_sum, kth_sum)
            left += 1
        average = maxi_sum / k   
        return average
        
