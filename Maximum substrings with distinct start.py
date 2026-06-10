class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = 0
        new_string = ""
        for i in s:
            if i not in new_string:
                new_string = new_string + i
                counts = counts + 1
        return counts        
        
