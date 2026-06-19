class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1] :
            return bool(1)
        else:
            return bool(0) 


        
