class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = sum(nums)
        b = a % k
        if b > a:
            return a 
        else:
            return b     

        
