class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        str_of_digit = str(digit)
        new_string =''.join(map(str,nums))
        return new_string.count(str_of_digit)
