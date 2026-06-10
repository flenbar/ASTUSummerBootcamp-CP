class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        counts_neg1 = operations.count("--X")
        counts_neg2 = operations.count("X--")
        counts_pos1 = operations.count("++X")
        counts_pos2 = operations.count("X++")
        return (counts_pos1 + counts_pos2)-(counts_neg1 + counts_neg2) 
        
